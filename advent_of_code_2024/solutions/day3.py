from advent_of_code_2024.problem import ProblemBase
import re

r = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")


def prod(l):
    p = 1
    for ll in l:
        p *= ll
    return p


class Day3_1(ProblemBase):
    def solve(self, input_str: str):
        found = r.findall(input_str)
        return sum(prod([int(n) for n in match]) for match in found)


class Day3_2(ProblemBase):
    def solve(self, input_str: str):
        pass
