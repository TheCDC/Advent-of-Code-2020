from advent_of_code_2022.problem import ProblemBase


def contains_fully(a_start, a_stop, b_start, b_stop):
    return a_start <= b_start and a_stop >= b_stop


def one_contains_another(a_start, a_stop, b_start, b_stop):
    return contains_fully(a_start, a_stop, b_start, b_stop) or contains_fully(
        b_start, b_stop, a_start, a_stop
    )


class Day4_1(ProblemBase):
    def solve(self, data: str):

        return sum(
            one_contains_another(
                *[int(i) for x in line.split(",") for i in x.split("-")]
            )
            for line in data.split("\n")
        )


class Day4_2(Day4_1):
    pass
