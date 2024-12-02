import collections
import itertools


def part_1(f):
    l1, l2 = list(), list()
    for line in f:
        (x1, x2) = line.split()
        l1.append(int(x1))
        l2.append(int(x2))

    l1, l2 = sorted(l1), sorted(l2)
    update = lambda total, i: total + abs(i[0] - i[1])
    acc = list(itertools.accumulate(zip(l1, l2), update, initial=0))
    return acc[-1]


def part_2(f):
    l1 = list()
    l2_freq = collections.defaultdict(int)
    for line in f:
        (x1, x2) = line.split()
        l1.append(int(x1))
        l2_freq[int(x2)] = l2_freq[int(x2)] + 1

    return list(
        itertools.accumulate(l1, lambda total, i: total + (i * l2_freq[i]), initial=0)
    )[-1]
