import time
import dataclasses
import itertools
import logging as log
from typing import Any, Optional


class DiskMap:
    def __init__(self, m):
        self.file_lengths = [int(c) for i, c in enumerate(m) if not i % 2]
        self.empty_lengths = [int(c) for i, c in enumerate(m) if i % 2]

    def values(self):
        id_iter = FileIdIter(self.file_lengths.copy())
        f_iter = id_iter.forward()
        b_iter = id_iter.backward()
        files_iter = iter(self.file_lengths)
        space_iter = iter(self.empty_lengths)
        try:
            while True:
                file_len = next(files_iter)
                for i in itertools.islice(f_iter, file_len):
                    yield i
                space_len = next(space_iter)
                for i in itertools.islice(b_iter, space_len):
                    yield i
        except StopIteration:
            return


class FileIdIter:
    def __init__(self, file_lengths):
        self.file_lengths = file_lengths
        self.f_idx = 0
        self.b_idx = len(self.file_lengths) - 1

    def forward(self):
        while self.f_idx < self.b_idx:
            while self.file_lengths[self.f_idx]:
                yield self.f_idx
                self.file_lengths[self.f_idx] -= 1
            self.f_idx += 1

    def backward(self):
        while self.b_idx > self.f_idx:
            while self.file_lengths[self.b_idx]:
                yield self.b_idx
                self.file_lengths[self.b_idx] -= 1
            self.b_idx -= 1


@dataclasses.dataclass
class FileBlock:
    id: int
    size: int
    next: Optional[Any] = None
    prev: Optional[Any] = None

    def __str__(self):
        return str(self.id) * self.size

    def __hash__(self):
        return hash(self.id)


@dataclasses.dataclass
class SpaceBlock:
    size: int
    next: Optional[Any] = None
    prev: Optional[Any] = None

    def __str__(self):
        return "." * self.size


class DiskChain:
    def __init__(self, m):
        space_iter = iter(m.empty_lengths)

        f = m.file_lengths[0]
        self.head = FileBlock(0, f)
        self.tail = None
        travel = self.head
        for i, f in enumerate(m.file_lengths[1:]):
            new = SpaceBlock(next(space_iter))
            travel.next = new
            new.prev = travel
            travel = travel.next
            new = FileBlock(i + 1, f)
            travel.next = new
            new.prev = travel
            travel = travel.next
        self.tail = travel

    def __str__(self):
        travel = self.head
        s = ""
        while travel:
            s += str(travel)
            travel = travel.next
        return s

    def defrag(self):
        front = self.head
        back = self.tail
        moved = set()

        while True:
            while back and not isinstance(back, FileBlock):
                back = back.prev

            if back in moved:
                return

            while front and (
                not isinstance(front, SpaceBlock) or front.size < back.size
            ):
                front = front.next
                if not front:
                    return

            if front.size < back.size:
                back = back.prev
                continue

            print(str(self))
            print("front:", front)
            print("back:", back)
            time.sleep(1)

            new_space = SpaceBlock(back.size)
            new_space.next = back.next
            new_space.prev = back.prev
            if back.prev:
                back.prev.next = new_space
            if back.next:
                back.next.prev = new_space

            if front.prev:
                front.prev.next = back
            back.prev = front

            if front.size == back.size:
                back.next = front.next
            else:
                back.next = SpaceBlock(front.size - back.size)
                back.next.prev = back
                back.next.next = front.next
                front.next.prev = back.next.next
                front.next = back

            moved.add(back)
            back = new_space.prev
            front = front.next.next
            print("front:", front)
            print("back:", back)


def part_1(f):
    m = DiskMap(f.read().strip())
    return sum(i * v for i, v in enumerate(m.values()))


def part_2(f):
    m = DiskMap(f.read().strip())
    chain = DiskChain(m)
    print(str(chain))
    chain.defrag()
    print(str(chain))
