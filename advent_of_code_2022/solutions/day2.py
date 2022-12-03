from ..problem import ProblemBase
from enum import Enum


class MovesEnum(Enum):
    rock = 1
    paper = 2
    scissors = 3


letter_to_move = {
    "a": MovesEnum.rock,
    "b": MovesEnum.paper,
    "c": MovesEnum.scissors,
    "x": MovesEnum.rock,
    "y": MovesEnum.paper,
    "z": MovesEnum.scissors,
}
moves_cycle = (MovesEnum.paper, MovesEnum.rock, MovesEnum.scissors)


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
    for m in moves_available:
        if beats(m, move) == result:
            return m
    raise RuntimeError("wtf")


def score_round(me: MovesEnum, them: MovesEnum):
    return me.value + 6 * beats(me, them) + 3 * (me == them)


class Day2_1(ProblemBase):
    def solve(self, data: str):
        score = 0
        for line in data.lower().split("\n"):
            them = letter_to_move[line[0]]
            me = letter_to_move[line[-1]]
            score += me.value + 6 * beats(me, them) + 3 * (me == them)
        return score


class Day2_2(ProblemBase):
    def solve(self, data: str):
        score = 0
        for line in data.lower().split("\n"):
            move_them = letter_to_move[line[0]]
            outcome_me = line[-1]
            if outcome_me == "y":  # we must draw
                move_me = move_them
            elif outcome_me == "x":  # we must lose
                move_me = search_beats_result(move_them, False)
            elif outcome_me == "z":  # we must win
                move_me = search_beats_result(move_them, True)
            else:
                RuntimeError("wtf")
            score += score_round(move_me, move_them)
        return score
