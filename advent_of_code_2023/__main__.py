from advent_of_code_2023.problem import ProblemBase
import advent_of_code_2023.solutions
from advent_of_code_2023.solutions import SOLUTIONS
from time import time
import sys
import pkgutil
from pathlib import Path
import os
import importlib
import inspect
from itertools import chain


def get_solutions():
    modules_imported = list(
        importlib.import_module(f"advent_of_code_2023.solutions.{x.name}")
        for x in pkgutil.iter_modules(
            [os.path.dirname(advent_of_code_2023.solutions.__file__)]
        )
    )
    dirs = [(module, dir(module)) for module in modules_imported]
    classes = list(
        sorted(
            chain.from_iterable(
                [
                    [
                        getattr(module, o)
                        for o in d
                        if inspect.isclass(getattr(module, o))
                        and issubclass(getattr(module, o), ProblemBase)
                        and getattr(module, o) is not ProblemBase
                    ]
                    for module, d in dirs
                ]
            ),
            key=str,
        )
    )
    classes = list(
        chain.from_iterable(
            [
                [
                    getattr(module, o)
                    for o in d
                    if inspect.isclass(getattr(module, o))
                    and issubclass(getattr(module, o), ProblemBase)
                    and getattr(module, o) is not ProblemBase
                ]
                for module, d in dirs
            ]
        )
    )
    return classes


def interative_pick(l: list) -> int:
    index = -1
    while index < 0 or (index >= len(l)):
        print("\n".join([f"{index}: {item}" for index, item in enumerate(l)]))
        try:
            index = int(input("Choose"))
        except ValueError:
            continue


def main():
    print("welcome to advent of code 2023")
    solutions = get_solutions()
    print('get_solutions',solutions)
    index = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    if index == -1:
        index = interative_pick([s.__name__ for s in solutions])
    problem_data = []
    print("Paste problem data lines:")
    line = None
    while True:
        try:
            problem_data.append(input())
        except (EOFError, KeyboardInterrupt):
            break
    ti = time()
    problem_instance: ProblemBase = solutions[index]()
    solution = problem_instance.solve("\n".join(problem_data))
    tf = time()

    print("Solution:", solution, "in", tf - ti)


if __name__ == "__main__":
    main()
