from advent_of_code_2023.problem import ProblemBase
from functools import reduce
from itertools import groupby

DIGITS = set(map(str, range(1, 10)))


# def flood_fill(grid: list[list[str]])->:
#     pass


def translate(c: str):
    if c.isdigit():
        return "d"
    elif c == ".":
        return "."
    else:
        return "s"


def flood_fill(grid: list[list[str]]) -> list[list[str]]:
    # fill out s over d i.e. sd -> ss
    queue = []
    offsets = [
        (-1, -1),
        (0, -1),
        (1, -1),  # row 1
        (-1, 0),
        (0, 0),
        (+1, 0),  # row 2
        (-1, 1),
        (0, 1),
        (+1, 1),  # row 3
    ]
    while True:
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == "s":
                    for o in offsets:
                        xnew = x + o[0]
                        ynew = y + o[1]
                        if (
                            xnew >= 0
                            and xnew < len(row)
                            and ynew >= 0
                            and ynew < len(grid)
                        ):
                            if grid[ynew][xnew] == "d":
                                queue.append((xnew, ynew))  # save coord for later
        if len(queue) == 0:
            return
        while queue:
            coord = queue.pop()
            grid[coord[1]][coord[0]] = "s"


def parse_input_to_grid(s: str):
    grid = [[translate(c) for c in list(row)] for row in s.split("\n")]
    return grid


class Day3_1(ProblemBase):
    def solve(self, input_str: str):
        grid_filled = parse_input_to_grid(input_str)
        print("\n".join(["".join(r) for r in grid_filled]), sep="\n")
        print("=" * len(grid_filled[0]))
        flood_fill(grid_filled)
        print("\n".join(["".join(r) for r in grid_filled]), sep="\n")
        grid_original = [list(row) for row in input_str.split("\n")]
        grid_final = parse_input_to_grid(input_str)
        for y, (row_original, row_filled) in enumerate(zip(grid_original, grid_filled)):
            # rewrite
            for x, (val_original, val_filled) in enumerate(
                zip(row_original, row_filled)
            ):
                if val_original.isdigit() and val_filled == "s":
                    grid_final[y][x] = val_original
                else:
                    grid_final[y][x] = " "
        print("=" * len(grid_final[0]))
        print("\n".join(["".join(r) for r in grid_final]), sep="\n")
        lines = " ".join(["".join(row) for row in grid_final])
        print("=" * len(grid_final[0]))
        print(sum(map(int, lines.split())))


# 473235 too low
# 476654 too low
# 521601 correct!


class Day3_2(ProblemBase):
    def solve(self, input_str: str):
        pass
