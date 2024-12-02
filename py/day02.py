import logging as log


def part_1(f):
    reports = [[int(i) for i in line.split()] for line in f]

    def is_safe(report):
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            if diff < 1 or diff > 3:
                return False
        return True

    ratings = [1 if is_safe(r) or is_safe(list(reversed(r))) else 0 for r in reports]
    return sum(ratings)
