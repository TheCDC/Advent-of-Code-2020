from advent_of_code_2020.problem import ProblemBase
from itertools import combinations


class Problem2(ProblemBase):
    def solve(self, input_string: str) -> int:
        nums = [int(l.strip()) for l in input_string.split()]
        for c in combinations(nums, 3):
            if(sum(c)) == 2020:
                return c[0] * c[1] * c[2]
        return 0
