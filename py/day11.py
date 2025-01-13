import abc
import collections
import logging as log


class Rule(abc.ABC):
    @abc.abstractmethod
    def applies(self, val):
        pass

    @abc.abstractmethod
    def convert(self, val):
        pass


class ZeroBecomesOne:
    def applies(self, val):
        return val == 0

    def convert(self, val):
        return [1]


class EvenSplit:
    def applies(self, val):
        return (len(str(val)) % 2) == 0

    def convert(self, val):
        s = str(val)
        half = len(s) // 2
        return [int(s[0:half]), int(s[half:])]


class MulBy2024:
    def applies(self, val):
        return True

    def convert(self, val):
        return [val * 2024]


class Stones:
    def __init__(self, initial, rules):
        self.vals = collections.defaultdict(int)
        for val in initial:
            self.vals[val] += 1
        self.rules = rules

    def blink(self):
        next_vals = collections.defaultdict(int)
        for val, count in self.vals.items():
            rule = next(filter(lambda rule: rule.applies(val), self.rules))
            for next_val in rule.convert(val):
                next_vals[next_val] += count
        self.vals = next_vals

    def count(self):
        return sum(self.vals.values())


def part_1(f):
    initial = [int(s) for s in f.read().strip().split()]
    stones = Stones(initial, [ZeroBecomesOne(), EvenSplit(), MulBy2024()])
    for i in range(0, 25):
        stones.blink()
    return str(stones.count())


def part_2(f):
    initial = [int(s) for s in f.read().strip().split()]
    stones = Stones(initial, [ZeroBecomesOne(), EvenSplit(), MulBy2024()])
    for i in range(0, 75):
        stones.blink()
    return str(stones.count())
