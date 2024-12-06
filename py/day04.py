import enum
import logging as log

from py import util


class Board:
    def __init__(self, contents):
        self._lines = contents.split()

    def __getitem__(self, key):
        if key.x < 0 or key.y < 0:
            return ""
        if key.x >= len(self._lines[0]) or key.y >= len(self._lines):
            return ""
        return self._lines[key.y][key.x]

    def word(self, location, direction, length):
        return "".join(self[location + direction.value * i] for i in range(length))

    def tlw_with_midpoint(self, location, direction):
        return "".join(
            [
                self[location - direction.value],
                self[location],
                self[location + direction.value],
            ]
        )

    def dimensions(self):
        return util.Coord(len(self._lines[0]), len(self._lines))


def part_1(f):
    board = Board(f.read())
    dims = board.dimensions()
    xmas_count = 0
    for x in range(dims.x):
        for y in range(dims.y):
            for dir in util.Direction:
                if board.word(util.Coord(x, y), dir, 4) == "XMAS":
                    xmas_count += 1
    return xmas_count


def part_2(f):
    board = Board(f.read())
    dims = board.dimensions()
    # If "MAS" is found in a primary direction (key) then check the secondary
    # directions (value) for another instance of "MAS".
    diagonal_dirs = {
        util.Direction.DOWN_LEFT: [util.Direction.DOWN_RIGHT, util.Direction.UP_LEFT],
        util.Direction.DOWN_RIGHT: [util.Direction.DOWN_LEFT, util.Direction.UP_RIGHT],
        util.Direction.UP_LEFT: [util.Direction.UP_RIGHT, util.Direction.DOWN_LEFT],
        util.Direction.UP_RIGHT: [util.Direction.UP_LEFT, util.Direction.DOWN_RIGHT],
    }
    mas_count = 0
    for x in range(dims.x):
        for y in range(dims.y):
            for dir, check_dirs in diagonal_dirs.items():
                if not board.tlw_with_midpoint(util.Coord(x, y), dir) == "MAS":
                    continue
                for check_dir in check_dirs:
                    if board.tlw_with_midpoint(util.Coord(x, y), check_dir) == "MAS":
                        mas_count += 1
                        break
    # This function double-counts every instance - for any given occurrence, it
    # counts where MAS is the primary and secondary instance
    return mas_count // 2
