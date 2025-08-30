import dataclasses

@dataclasses.dataclass(frozen=True)
class Coord:
    x: int
    y: int

@dataclasses.dataclass
class Stats:
    perimeter: int
    color: int


def part_1(f):
    field = [l for l in f.read().splitlines()]


def part_2(f):
    pass
