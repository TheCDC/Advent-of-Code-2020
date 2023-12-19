from advent_of_code_2023.problem import ProblemBase


def parse_problem(s):
    lines = s.split("\n")
    for l in lines:
        a = l.split(":")
        a1 = a[0]
        a2 = a[1]
        cardnum = int(a1.split()[1])
        b = a2.split("|")
        b1 = list(map(int, b[0].strip().split()))
        b2 = list(map(int, b[1].strip().split()))
        yield (cardnum, b1, b2)


def count_winners(game: tuple[int, list[int], list[int]]):
    targets = set(game[1])
    return (game, sum(1 for n in game[2] if n in targets))


def score_count_winners(n: int) -> int:
    return 2 ** (n - 1) if n > 0 else 0


def get_copies_numbers(game: tuple[int, list[int], list[int]]):
    yield from (n + game[0] + 1 for n in range(count_winners(game)[1]))


class Day4_1(ProblemBase):
    def solve(self, input_str: str):
        parsed = list(map(count_winners, parse_problem(input_str)))
        scored = [(score_count_winners(s[-1]), s) for s in parsed]
        print(*scored, sep="\n")
        print(sum(s[0] for s in scored))
        # 28750 correct!


class Day4_2(ProblemBase):
    def solve(self, input_str: str):
        parsed = list(map(count_winners, parse_problem(input_str)))

        queue = parsed[:]
        parsed_initial = [[p, 1] for p in parsed[:]]
        # node_values: dict[int:int] = dict()

        for index, node_child in reversed(list(enumerate(parsed_initial))):
            id_child = node_child[0][0][0]
            for index_parent, node_parent in enumerate(parsed_initial[0:index]):
                ids_children = set(n - 1 for n in get_copies_numbers(node_parent[0][0]))
                if id_child in ids_children:
                    node_parent[-1] += node_child[-1]
        print(*parsed_initial, sum(p[-1] for p in parsed_initial), sep="\n")
        return

        counted = 0
        while queue:
            counted += 1
            game_scored = queue.pop()
            game = game_scored[0]
            cardnum = game[0]
            score = game_scored[1]
            copies = list(get_copies_numbers(game))
            if counted % 100000 == 0:
                print(len(queue))
            # print(cardnum, score, copies)
            queue.extend([parsed[i - 1] for i in copies])
        return counted
        # 10212704 correct!
