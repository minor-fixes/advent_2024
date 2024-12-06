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

    def __getitem__(self, key):
        if key.x < 0 or key.y < 0:
            return None
        if key.x >= len(self.board[0]) or key.y >= len(self.board):
            return None
        return self.board[key.y][key.x]

    def __setitem__(self, key, val):
        if key.x < 0 or key.y < 0:
            raise IndexError()
        if key.x >= len(self.board[0]) or key.y >= len(self.board):
            raise IndexError()
        self.board[key.y][key.x] = val

    def change_dir(self):
        self.current_dir = (self.current_dir + 1) % len(_DIRS)

    def peek(self):
        next = self.current + _DIRS[self.current_dir].value
        return self[next]

    def step(self):
        self[self.current] = "X"
        self.current = self.current + _DIRS[self.current_dir].value
        self[self.current] = "X"

    def mark_count(self):
        return sum(1 if s == "X" else 0 for r in self.board for s in r)


def part_1(f):
    board = Board(f.read())
    while True:
        next = board.peek()
        if not next:
            return board.mark_count()
        if next == "#":
            board.change_dir()
        else:
            board.step()
