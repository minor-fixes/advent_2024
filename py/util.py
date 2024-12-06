import enum


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        return Coord(self.x * scale, self.y * scale)


class Direction(enum.Enum):
    UP = Coord(0, -1)
    UP_RIGHT = Coord(1, -1)
    RIGHT = Coord(1, 0)
    DOWN_RIGHT = Coord(1, 1)
    DOWN = Coord(0, 1)
    DOWN_LEFT = Coord(-1, 1)
    LEFT = Coord(-1, 0)
    UP_LEFT = Coord(-1, -1)
