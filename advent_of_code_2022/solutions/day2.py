from ..problem import ProblemBase
from enum import Enum


class MovesEnum(Enum):
    paper = 2  # paper beats rock
    rock = 1  # rock beats scissors
    scissors = 3  # scissors beats paper


letter_to_move = {
    "a": MovesEnum.rock,
    "b": MovesEnum.paper,
    "c": MovesEnum.scissors,
    "x": MovesEnum.rock,
    "y": MovesEnum.paper,
    "z": MovesEnum.scissors,
}
moves_cycle = tuple(MovesEnum)


def beats(move_a: MovesEnum, move_b: MovesEnum) -> bool:

    idx_a = moves_cycle.index(move_a)
    idx_b = moves_cycle.index(move_b)
    diff = 0

    while (idx_a + diff) % len(moves_cycle) != idx_b:
        diff += 1
    if diff < 0 or 2 < diff:
        raise RuntimeError("logic error")
    return diff == 1


def search_beats_result(move: MovesEnum, result: bool) -> MovesEnum:
    moves_available = set(MovesEnum) - {move}
    options = [m for m in moves_available if beats(m, move) == result]
    if len(options) != 1:
        raise RuntimeError("Logic erorr")
    return options[0]


def score_round(me: MovesEnum, them: MovesEnum):
    return me.value + 6 * beats(me, them) + 3 * (me == them)


class Day2_1(ProblemBase):
    def solve(self, data: str):
        return sum(
            score_round(letter_to_move[line[-1]], letter_to_move[line[0]])
            for line in data.lower().split("\n")
        )


class Day2_2(ProblemBase):
    def solve(self, data: str):
        score = 0
        for line in data.lower().split("\n"):
            move_them = letter_to_move[line[0]]
            move_me = {
                "y": lambda: move_them,  # draw
                "x": lambda: search_beats_result(move_them, False),  # lose
                "z": lambda: search_beats_result(move_them, True),  # win
            }[line[-1]]()
            score += score_round(move_me, move_them)
        return score
