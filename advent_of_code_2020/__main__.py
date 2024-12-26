from advent_of_code_2020.problem import ProblemBase
import advent_of_code_2020.solutions as solutions
from advent_of_code_2020.solutions import SOLUTIONS
from time import time
print("welcome to advent of code 2020")
index = -1
while index < 0 or (index >= len(SOLUTIONS)):
    print("\n".join([f"{index}: {item.__name__}" for index, item in enumerate(
        SOLUTIONS)]))
    try:
        index = int(input("Choose"))
    except ValueError:
        continue
    problem_data = []
    print("Paste problem data lines:")
    line = None
    while True:
        try:

            problem_data.append(input())
        except EOFError:
            break
    ti = time()
    problem_instance: ProblemBase = SOLUTIONS[index]()
    solution = problem_instance.solve("\n".join(problem_data))
    tf = time()

    print("Solution:", solution, "in", tf-ti)
