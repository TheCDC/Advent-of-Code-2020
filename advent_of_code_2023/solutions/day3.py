from typing import Any, Generator
from advent_of_code_2023.problem import ProblemBase
from copy import deepcopy

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


def iterate_neighbors(
    grid: list[list[Any]],
    x,
    y,
) -> Generator[tuple[Any, int, int], Any, None]:
    offsets = [
        (-1, -1),
        (0, -1),
        (1, -1),  # row 1
        #
        (-1, 0),
        (0, 0),
        (+1, 0),  # row 2
        #
        (-1, 1),
        (0, 1),
        (+1, 1),  # row 3
    ]
    row = grid[y]
    for o in offsets:
        xnew = x + o[0]
        ynew = y + o[1]
        if 0 <= xnew < len(row) and 0 <= ynew < len(grid):
            valnew = grid[ynew][xnew]
            ret = (valnew, xnew, ynew)
            yield ret


def flood_fill(grid: list[list[str]]) -> list[list[str]]:
    # fill out s over d i.e. sd -> ss
    queue = []
    while True:
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == "s":
                    for neighbor in iterate_neighbors(grid, x, y):
                        if neighbor[0] == "d":
                            queue.append(
                                (neighbor[1], neighbor[2])
                            )  # save coord for later
        if len(queue) == 0:
            return
        while queue:
            coord = queue.pop()
            grid[coord[1]][coord[0]] = "s"


def iterate_grid(grid: list[list]):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            yield (val, x, y)


def relabel_numbers_unique(
    grid_masked: list[list[str]], grid_original: list[list[str]]
):
    # none-d,d-d,d-notnone
    gridnew = deepcopy(grid_masked)
    count = 0
    prev = (None, 0, 0)
    numbers: dict[int, int] = dict()
    digits: list[str] = []
    for val, x, y in iterate_grid(grid_masked):
        val_old = grid_original[y][x]
        if val == "d":
            if prev[0] != "d":
                count += 1
                digits = [str(val_old)]
            else:
                digits.append(str(val_old))
            gridnew[y][x] = count
        else:
            numbers.update({count: int("".join(digits))})
        prev = val
    return numbers, gridnew


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
        grid_filled = parse_input_to_grid(input_str)
        grid_original = [list(row) for row in input_str.split("\n")]

        numbers, grid_labelled = relabel_numbers_unique(grid_filled, grid_original)
        # print(*grid_labelled, sep="\n")
        edges = []
        for val, x, y in iterate_grid(grid_labelled):
            if val != "s":
                continue
            neighbors = list(iterate_neighbors(grid_labelled, x, y))
            neighbors_ids = set(n[0] for n in neighbors if isinstance(n[0], int))
            if len(neighbors_ids) == 2:
                # this
                edges.append(tuple(sorted(neighbors_ids)))
        # print(edges, numbers)
        print(f"Found {len(numbers)} numbers")
        print(f"Found {len(edges)} gears")
        print(sum(numbers[e[0]] * numbers[e[1]] for e in edges))
        # 80694070 correct first try!
