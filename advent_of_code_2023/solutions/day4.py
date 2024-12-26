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

        node_values: dict[int:int] = dict()
        leaves = [p for p in parsed if p[-1] == 0]
        node_values.update({l[0][0]: 1 for l in leaves})
        # print("=" * 30)
        # print("leaves", *sorted(node_values.items()))
        while len(node_values) != len(parsed):  # until all nodes have been resolved
            leaves_resolved = [  # the new leaf nodes are
                p  # each game where
                for p in parsed
                if p[0][0] not in node_values  # its sum hasn't been resolved
                and all(
                    x in node_values for x in get_copies_numbers(p[0])
                )  # and all its children have been resolved
            ]
            updates = {  # resolve the new leaf nodes by
                l[0][0]: sum(
                    node_values[i] for i in get_copies_numbers(l[0])
                )  # summing values of all child nodes
                + 1  # plus one to count this node
                for l in leaves_resolved
            }
            node_values.update(updates)
        # print("=" * 30)
        # print(*(i for i in sorted(node_values.items())), sep="\n")
        result = sum(b for _, b in node_values.items())
        return result
        # 10212704 correct!
