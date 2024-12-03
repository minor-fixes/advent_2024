import logging as log
import re


def _strip_disabled(line: str):
    if (loc := line.find("do()")) == -1:
        return ""
    else:
        return line[loc + len("do()") :]


def part_1(f):
    mul_re = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    matches = mul_re.findall(f.read())
    return sum(int(m[0]) * int(m[1]) for m in matches)


def part_2(f):
    mul_re = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    lines = f.read().split("don't()")
    sanitized = lines[0] + "".join(_strip_disabled(l) for l in lines[1:])
    matches = mul_re.findall(sanitized)
    return sum(int(m[0]) * int(m[1]) for m in matches)
