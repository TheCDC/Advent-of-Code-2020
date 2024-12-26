from advent_of_code_2024.problem import ProblemBase
import re

r = re.compile(r"(mul\(([0-9]{1,3}),([0-9]{1,3})\))")
r2 = re.compile(r"(do\(\)|don't\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\))")


def prod(l):
    p = 1
    for ll in l:
        p *= ll
    return p


class Day3_1(ProblemBase):
    def solve(self, input_str: str):
        found = r.findall(input_str)
        return sum(prod([int(n) for n in match[1:]]) for match in found)


class Day3_2(ProblemBase):
    def solve(self, input_str: str):
        found = r2.findall(input_str)
        enabled = True
        s = 0
        for f in found:
            if f[0].startswith("do()"):
                enabled = True
            elif f[0].startswith("don't()"):
                enabled = False
            elif f[0].startswith("mul("):
                mult = int(f[1]) * int(f[2])
                s += mult * enabled
            # print(f, s, enabled)
        return s
