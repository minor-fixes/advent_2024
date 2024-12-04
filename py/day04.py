import enum
import logging as log

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x-other.x, self.y-other.y)

    def __mul__(self, scale):
        return Coord(self.x*scale, self.y*scale)

class Direction(enum.Enum):
    UP = Coord(0, -1)
    UP_RIGHT = Coord(1, -1)
    RIGHT = Coord(1, 0)
    DOWN_RIGHT = Coord(1, 1)
    DOWN = Coord(0, 1)
    DOWN_LEFT = Coord(-1, 1)
    LEFT = Coord(-1, 0)
    UP_LEFT = Coord(-1, -1)

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
        return "".join(self[location+direction.value*i] for i in range(length))

    def tlw_with_midpoint(self, location, direction):
        return "".join([
            self[location-direction.value],
            self[location],
            self[location+direction.value],
        ])

    def dimensions(self):
        return Coord(len(self._lines[0]), len(self._lines))


def part_1(f):
    board = Board(f.read())
    dims = board.dimensions()
    xmas_count = 0
    for x in range(dims.x):
        for y in range(dims.y):
            for dir in Direction:
                if board.word(Coord(x, y), dir, 4) == "XMAS":
                    xmas_count += 1
    return xmas_count

def part_2(f):
    board = Board(f.read())
    dims = board.dimensions()
    # If "MAS" is found in a primary direction (key) then check the secondary
    # directions (value) for another instance of "MAS".
    diagonal_dirs = {
        Direction.DOWN_LEFT: [Direction.DOWN_RIGHT, Direction.UP_LEFT],
        Direction.DOWN_RIGHT: [Direction.DOWN_LEFT, Direction.UP_RIGHT],
        Direction.UP_LEFT: [Direction.UP_RIGHT, Direction.DOWN_LEFT],
        Direction.UP_RIGHT: [Direction.UP_LEFT, Direction.DOWN_RIGHT],
    }
    mas_count = 0
    for x in range(dims.x):
        for y in range(dims.y):
            for dir, check_dirs in diagonal_dirs.items():
                if not board.tlw_with_midpoint(Coord(x, y), dir) == "MAS":
                    continue
                for check_dir in check_dirs:
                    if board.tlw_with_midpoint(Coord(x, y), check_dir) == "MAS":
                        mas_count += 1
                        break
    # This function double-counts every instance - for any given occurrence, it
    # counts where MAS is the primary and secondary instance
    return mas_count // 2