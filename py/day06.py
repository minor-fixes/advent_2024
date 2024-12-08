import time
import logging as log

from py import util

_DIRS = [
    util.Direction.UP,
    util.Direction.RIGHT,
    util.Direction.DOWN,
    util.Direction.LEFT,
]


class Board:
    def __init__(self, contents):
        self.board = [list(s) for s in contents.split()]
        self.current_dir = 0
        idx = "".join(contents.split()).find("^")
        row_len = len(self.board[0])
        self.current = util.Coord(idx % row_len, idx // row_len)
        self.board[self.current.y][self.current.x] = "X"

    def __getitem__(self, key):
        if key not in self:
            return None
        return self.board[key.y][key.x]

    def __setitem__(self, key, val):
        if key not in self:
            raise IndexError()
        self.board[key.y][key.x] = val

    def __contains__(self, key):
        return (
            key.x >= 0
            and key.x < len(self.board[0])
            and key.y >= 0
            and key.y < len(self.board)
        )

    def change_dir(self):
        self.current_dir = (self.current_dir + 1) % len(_DIRS)
        return self._next_coord()

    def _next_coord(self):
        next = self.current + _DIRS[self.current_dir].value
        return next if next in self else None

    def step(self):
        next = self._next_coord()
        log.info("Next: %s", next)
        if not next:
            return None
        if self[next] in ("#", "+"):
            self[next] = "+"
            next = self.change_dir()
            if not next:
                return None
        self.current = next
        self[self.current] = "X"
        return self.current

    def mark_count(self):
        return sum(1 if s == "X" else 0 for r in self.board for s in r)

    def obstruction_causes_loop(self):
        if (next := self._next_coord()) and self[next] not in ("#", "+"):
            next_dir = _DIRS[(self.current_dir + 1) % len(_DIRS)].value
            travel = self.current
            while lookahead := self[travel + next_dir]:
                if lookahead == "+":
                    return True
                if lookahead == "#":
                    return False
                travel += next_dir
        return False


def part_1(f):
    board = Board(f.read())
    while board.step():
        pass
    return board.mark_count()


def part_2(f):
    board = Board(f.read())
    obstructions = set()
    while loc := board.step():
        if board.obstruction_causes_loop():
            obstructions.add(loc)
    return len(obstructions)
