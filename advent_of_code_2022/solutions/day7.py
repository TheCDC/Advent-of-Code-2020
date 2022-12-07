from advent_of_code_2022.problem import ProblemBase
from typing import Iterable, Optional
from dataclasses import dataclass
from enum import Enum


class FileType(Enum):
    directory = 0
    file = 1


@dataclass
class Node:
    name: str
    children: list["Node"]
    parent: "Node"
    file_type: FileType
    size: Optional[int] = None

    def get_children(self, name: str) -> list["Node"]:
        existing = [c for c in self.children if c.name == name]
        return existing

    def upsert_child(
        self, name: str, size: int, file_type: FileType, children=None
    ) -> "Node":
        children = children if children else []
        existing = self.get_children(name)
        if existing:
            matched = existing[0]
            matched.name = name
            matched.children = children
            matched.size = size
            matched.file_type = file_type
            matched.parent = self
            return matched
        node_new = Node(
            name=name, size=size, children=children, file_type=file_type, parent=self
        )
        self.children.append(node_new)
        return node_new

    def pretty(self, depth=0):
        yield " ".join(
            [
                "-" * depth,
                "[ ]" if self.file_type == FileType.directory else "[x]",
                self.name,
            ]
        )
        for c in self.children:
            yield from c.pretty(depth + 1)

    def __str__(self, depth=-0) -> str:
        return "\n".join(self.pretty())


class Day7_1(ProblemBase):
    def lines(self, data: str) -> Iterable[str]:
        yield from data.split("\n")

    def solve(self, input_string: str) -> int:
        node = Node("/", [], None, FileType.directory)
        root = node
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
                        elif dir_target == "/":
                            node = root
                        else:
                            # known directory

                            node = node.get_children(name=dir_target)[0]
                elif tokens[0].isdigit():
                    # a file
                    size = int(tokens[0])
                    name = tokens[1]
                    leaf = node.upsert_child(
                        name=name, size=size, file_type=FileType.file
                    )
                    # traverse ancestors and update size
                    while leaf.parent:
                        leaf.parent.size = (
                            leaf.parent.size if leaf.parent.size else 0
                        ) + size
                        leaf = leaf.parent
                elif tokens[0] == "dir":
                    # directory
                    name = tokens[1]
                    node.upsert_child(
                        name=name, size=None, file_type=FileType.directory
                    )

            except StopIteration:
                break
        print(root)
        stack = [root]
        s = 0
        while stack:
            node = stack.pop()
            if node.file_type == FileType.directory and node.size <= 100000:
                s += node.size
            for c in node.children:
                stack.append(c)
        # 77891 low
        # 1792222 correct
        return s


class Day7_2(Day7_1):
    def solve(self, input_string: str) -> int:
        pass
