from advent_of_code_2023.problem import ProblemBase
from collections import Counter
from functools import reduce
from itertools import groupby


def process_game_line(line: str):
    try:
        game_id = int(line.split(":")[0].split(" ")[1])
    except IndexError:
        pass
    rounds = line.split(":")[1].split(";")
    pulls = [pull.strip() for r in rounds for pull in r.strip().split(",")]
    pairs = sorted(
        [(p.split(" ")[1], int(p.split(" ")[0])) for p in pulls], key=lambda t: t[0]
    )
    groups = groupby(pairs, key=lambda t: t[0])
    biggest = dict([max(g[1], key=lambda t: t[1]) for g in groups])
    return (game_id, biggest)


def game_is_possible(game: tuple[int, dict]):
    return game["red"] <= 12 and game["green"] <= 13 and game["blue"] <= 14


class Day2_1(ProblemBase):
    def solve(self, input_str: str):
        processed = [process_game_line(line) for line in input_str.split("\n")]
        matched = [game for game in processed if game_is_possible(game[1])]
        print(*matched, sep="\n")
        print(sum(m[0] for m in matched))


class Day2_2(ProblemBase):
    def solve(self, input_str: str):
        pass
