from advent_of_code_2020.problem import ProblemBase


class Problem1(ProblemBase):
    def solve(self, input_string: str):
        nums = [int(l.strip()) for l in input_string.split()]
        num_set = set(nums)
        for n in num_set:
            target_n = 2020-n
            if target_n in num_set:
                return n*target_n
        return 0
