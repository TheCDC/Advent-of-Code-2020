from advent_of_code_2022.problem import ProblemBase
from pprint import pprint

CHARS_IGNORED = set("[] ")


class Day5_1(ProblemBase):
    def lines(self, data: str) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
        s_board, s_moves = data.split("\n\n")[:2]
        board = [
            col
            for col in [
                [char for char in line if char not in CHARS_IGNORED][::-1]
                for line in list(zip(*(s_board.split("\n")[:-1])))
                # if char not in CHARS_IGNORED
            ]
            if col
        ]
        moves = [
            tuple(int(group) for group in line.split(" ") if group.isdigit())[:3]
            for line in s_moves.split("\n")
        ]
        return board, moves

    def solve(self, data: str) -> str:
        board, moves = self.lines(data)
        for m in moves:
            count, m_from, m_to = m
            for _ in range(count):
                board[m_to - 1].append(board[m_from - 1].pop())
        return "".join([c[-1] for c in board])


class Day5_2(Day5_1):
    def solve(self, data: str) -> str:
        board, moves = self.lines(data)
        for m in moves:
            m_count, m_from, m_to = m
            # pprint((list(enumerate(board)), m))
            substack = board[m_from - 1][-m_count:]
            board[m_to - 1] = board[m_to - 1] + substack
            board[m_from - 1] = board[m_from - 1][:-m_count]
        return "".join([c[-1] for c in board])
