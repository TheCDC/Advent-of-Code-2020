from advent_of_code_2022.problem import ProblemBase
from functools import reduce
from itertools import islice, groupby


def get_error(compartments: tuple[str, str]) -> str:
    return (set(compartments[0]) & set(compartments[1])).pop()


def get_item_priority(char: str) -> int:
    return ord(char.lower()) - 97 + 1 + 26 * char.isupper()


class Day3_1(ProblemBase):
    def lines(self, data: str) -> list[tuple[str, str]]:
        for line in data.split("\n"):
            ll = len(line)
            yield (line[: ll // 2], line[ll // 2 :])

    def solve(self, data: str):
        return sum(get_item_priority(get_error(line)) for line in self.lines(data))


class Day3_2(Day3_1):
    def solve(self, data: str):
        lines = self.lines(data)
        return sum(
            get_item_priority(
                reduce(lambda a, b: (a & b), (set("".join(tt[1])) for tt in t[1])).pop()
            )
            for t in groupby(enumerate(lines), (lambda tup: tup[0] // 3))
        )
