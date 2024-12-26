from advent_of_code_2022.problem import ProblemBase
from itertools import permutations


def contains_fully(a_start, a_stop, b_start, b_stop):
    return a_start <= b_start and a_stop >= b_stop


def overlaps(a_start, a_stop, b_start, b_stop):
    """
    a      a
      b  b
    a  a
     b   b
     a a
    b b
    """
    pairs = [(a_start, a_stop), (b_start, b_stop)]

    s = [
        sorted(pairs, key=lambda t: t[0])[0],
        sorted(pairs, key=lambda t: t[1], reverse=True)[0],
    ]
    return s[0][1] >= s[1][0]


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
    # 723 too low
    # try 837
    # correct 837
    def solve(self, data: str):
        return sum(
            overlaps(*[int(i) for x in line.split(",") for i in x.split("-")])
            for line in data.split("\n")
        )
