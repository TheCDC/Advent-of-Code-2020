from advent_of_code_2023.problem import ProblemBase

digit_words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


class Day1_1(ProblemBase):
    def solve(self, input_str: str):
        translate = str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz")
        ns = [l.translate(translate) for l in input_str.split("\n")]
        for l in ns:
            assert (len(l) == 2 for l in ns)
        return sum(int(s[0] + s[-1]) for s in ns)


class Day1_2(ProblemBase):
    def solve(self, input_str: str):
        s = 0
        for l in input_str.split("\n"):
            found = sorted(
                [(index, k) for k in digit_words for index in find_all(l, k)],
                key=lambda t: t[0],
            )
            num = digit_words[found[0][1]] * 10 + digit_words[found[-1][1]]
            s += num
        return s
