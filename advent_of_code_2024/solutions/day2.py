from advent_of_code_2024.problem import ProblemBase


def check(report: list[int]):
    # True=Safe
    deltas = [b - a for a, b in zip(report, report[1:])]
    return all(abs(d) >= 1 and abs(d) <= 3 for d in deltas) and (
        all(d > 0 for d in deltas) or all(d < 0 for d in deltas)
    )
def check_count(report: list[int]):
    # True=Safe
    if check(report):
        return True
    for index in range(len(report)):
        if check(report[:index]+report[index+1:]):
            return True
    return False
class Day2_1(ProblemBase):
    def solve(self, input_str: str):
        reports = [[int(i) for i in line.split()] for line in input_str.split("\n")]
        return sum(check(r) for r in reports)


class Day2_2(ProblemBase):
    def solve(self, input_str: str):
        reports = [[int(i) for i in line.split()] for line in input_str.split("\n")]
        return sum(check_count(r) for r in reports)


