from advent_of_code_2024.problem import ProblemBase
class Day1_1(ProblemBase):
    def solve(self, input_str: str):
        aa = []
        bb = []
        for line in input_str.split('\n'):
            a,b = [int(i) for i in line.split() if line ]
            aa.append(a)
            bb.append(b)
        aa.sort()
        bb.sort()
        distances = (abs(a-b) for a,b in zip(aa,bb))
        return sum(distances)
class Day1_2(ProblemBase):
    def solve(self, input_str: str):
        pass
