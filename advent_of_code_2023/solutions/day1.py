from advent_of_code_2023.problem import ProblemBase

digit_words = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def wordtodigit(s: str):
    sf = s
    while True:
        found = sorted(
            [(sf.find(k), k) for k in digit_words if sf.find(k) > -1],
            key=lambda t: t[0],
            reverse=True,
        )
        print(found)
        if len(found) == 0:
            break
        sf = sf.replace(found[0][1], digit_words[found[0][1]], 1)
    return sf


class Day1_1(ProblemBase):
    def solve(self, input_str: str):
        translate = str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz")
        ns = [l.translate(translate) for l in input_str.split("\n")]
        for l in ns:
            assert (len(l) == 2 for l in ns)
        return sum(int(s[0] + s[-1]) for s in ns)


class Day1_2(ProblemBase):
    def solve(self, input_str: str):
        translate = str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz")
        ns = [wordtodigit(l).translate(translate) for l in input_str.split("\n")]
        for l in ns:
            assert (len(l) == 2 for l in ns)
        # print(*ns, sep="\n")
        return sum(int(s[0] + s[-1]) for s in ns)
