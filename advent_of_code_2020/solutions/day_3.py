from advent_of_code_2020.problem import ProblemBase


class Point:
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y


class Slope:
    def __init__(self, right: int, down: int) -> None:
        super().__init__()
        self.right = right
        self.down = down


class Day3Part1(ProblemBase):
    def solve(self, input_string: str):
        position = Point(0, 0)
        grid = [list(line) for line in input_string.split("\n")]
        tree_count = 0
        while position.y < len(grid):
            if grid[position.y][position.x] == '#':
                tree_count += 1
            newx = (position.x + 3) % len(grid[0])
            position.x = newx
            position.y += 1
        return tree_count


class Day3Part2(ProblemBase):
    def solve(self, input_string: str):
        slopes = [
            Slope(1, 1),
            Slope(3, 1),
            Slope(5, 1),
            Slope(7, 1),
            Slope(1, 2),
        ]
        grid = [list(line) for line in input_string.split("\n")]
        slope_tree_counts_product = 1
        for slope in slopes:
            position = Point(0, 0)
            tree_count_this_slope = 0
            while position.y < len(grid):
                if grid[position.y][position.x] == '#':
                    tree_count_this_slope += 1
                newx = (position.x + slope.right) % len(grid[0])
                position.x = newx
                position.y += slope.down
            slope_tree_counts_product *= tree_count_this_slope
        return slope_tree_counts_product
