from advent_of_code_2022.problem import ProblemBase


class Day1_1(ProblemBase):
    def solve(self, input_str: str):
        elves = []
        count = 0
        for line in input_str.split("\n"):
            if not line:
                elves.append(count)
                count = 0
            else:
                count += int(line)
        return max(elves)


class Day1_2(ProblemBase):
    def solve(self, input_str: str):
        elves = []
        count = 0
        for line in input_str.split("\n"):
            if not line:
                elves.append(count)
                count = 0
            else:
                count += int(line)
        elves_sorted = sorted(elves, reverse=True)
        return sum(elves_sorted[:3])
