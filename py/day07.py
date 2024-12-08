import itertools


class Equation:
    def __init__(self, line):
        result, operands = line.split(": ")
        self.result = int(result)
        self.operands = [int(o) for o in operands.split(" ")]

    def calibration_result(self, ops):
        for op_combo in itertools.product(ops, repeat=len(self.operands) - 1):
            cr = self.operands[0]
            for i, operand in enumerate(self.operands[1:]):
                if op_combo[i] == "+":
                    cr += operand
                elif op_combo[i] == "*":
                    cr *= operand
                elif op_combo[i] == "|":
                    cr = int(f"{cr}{operand}")
            if cr == self.result:
                return self.result
        return 0


def part_1(f):
    equations = [Equation(l) for l in f.read().splitlines()]
    return sum(e.calibration_result("+*") for e in equations)


def part_2(f):
    equations = [Equation(l) for l in f.read().splitlines()]
    return sum(e.calibration_result("+*|") for e in equations)
