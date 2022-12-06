from advent_of_code_2022.problem import ProblemBase
from itertools import takewhile


def test_window(data: str):
    return len(set(data)) == len(data)


class Day6_1(ProblemBase):
    def solve(self, input_string: str, window_size=4) -> int:
        window_target = list(
            enumerate(
                takewhile(
                    lambda window: not test_window(window),
                    [
                        input_string[start : start + window_size]
                        for start in range(len(input_string))
                    ],
                )
            )
        )[-1]
        window_target_index = window_target[0] + 1
        # 1076 low
        # 1080
        return window_target_index + window_size


class Day6_2(Day6_1):
    def solve(self, input_string: str, window_size=14) -> int:
        return super().solve(input_string, window_size=window_size)
