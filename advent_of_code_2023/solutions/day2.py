from advent_of_code_2023.problem import ProblemBase
from functools import reduce
from itertools import groupby


def process_game_line(line: str, func=max):
    game_id = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].split(";")
    pulls = [pull.strip() for r in rounds for pull in r.strip().split(",")]
    pairs = sorted(
        [(p.split(" ")[1], int(p.split(" ")[0])) for p in pulls], key=lambda t: t[0]
    )
    groups = groupby(pairs, key=lambda t: t[0])
    biggest = dict([func(g[1], key=lambda t: t[1]) for g in groups])
    return (game_id, biggest)


def game_is_possible(game: tuple[int, dict]):
    return game["red"] <= 12 and game["green"] <= 13 and game["blue"] <= 14


def cubes_power(pulls: dict) -> int:
    assert len(pulls.values()) > 1
    return reduce(lambda a, b: a * b, pulls.values(), 1)


class Day2_1(ProblemBase):
    def solve(self, input_str: str):
        processed = [process_game_line(line) for line in input_str.split("\n")]
        matched = [game for game in processed if game_is_possible(game[1])]
        print(*matched, sep="\n")
        print(sum(m[0] for m in matched))


class Day2_2(ProblemBase):
    def solve(self, input_str: str):
        processed = [
            process_game_line(line, func=max) for line in input_str.split("\n")
        ]
        powers = [cubes_power(game[1]) for game in processed]
        print(*powers, sep="\n")
        print(sum(powers))
