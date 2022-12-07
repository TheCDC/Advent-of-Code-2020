from advent_of_code_2022.problem import ProblemBase
from typing import Iterable, Optional
from dataclasses import dataclass


@dataclass
class Node:
    name: str
    children: list["Node"]
    parent: "Node"
    size: Optional[int] = None

    def get_children(self, name: str) -> list["Node"]:
        existing = [c for c in self.children if c.name == name]
        return existing

    def upsert_child(self, name: str, size: int, children=None) -> "Node":
        existing = self.get_children(name)
        if existing:
            matched = existing[0]
            matched.name = name
            matched.children = children
            matched.size = size
            matched.parent = self

    def pretty(self, depth=0):
        yield self.name
        for c in self.children:
            yield " ".join["-" * depth, c.pretty(depth + 1)]

    def __str__(self, depth=-0) -> str:
        return "\n".join(self.pretty)


class Day7_1(ProblemBase):
    def lines(self, data: str) -> Iterable[str]:
        yield from data.split("\n")

    def solve(self, input_string: str) -> int:
        node = Node("/", [], None)
        lines = self.lines(input_string)
        while True:
            try:
                line = next(lines)
                tokens = line.split(" ")
                if tokens[0] == "$":
                    # a command
                    command = tokens[1]
                    args = tokens[1:]
                    if command == "cd":
                        dir_target = args[1]
                        if dir_target == "..":
                            node = node.parent
                        else:
                            node = node.get_children(name=dir_target)[0]
                elif tokens[0].isdigit():
                    # a file
                    size = tokens[0]
                    name = tokens[1]
                    node.upsert_child(name=name, size=size)
                elif tokens[0] == "dir":
                    # directory
                    node.upsert_child(name=name, size=None)

            except StopIteration:
                break


class Day7_2(Day7_1):
    def solve(self, input_string: str) -> int:
        pass
