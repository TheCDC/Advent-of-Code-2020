from advent_of_code_2022.problem import ProblemBase
from typing import Iterable, Optional, Callable
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
                f"{self.size}",
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

    def get_graph(self, data: str):
        node = Node("/", [], None, FileType.directory)
        root = node
        lines = self.lines(data)
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
        return root

    def filter_nodes(self, predicate: Callable[[Node], bool], node: Node):
        stack = [node]
        while stack:
            node = stack.pop()
            if predicate(node):
                yield node
            for c in node.children:
                stack.append(c)

    def solve(self, input_string: str) -> int:
        root = self.get_graph(input_string)
        print(root)
        s = 0
        return sum(
            n.size
            for n in self.filter_nodes(
                lambda node: node.file_type == FileType.directory
                and node.size <= 100000,
                root,
            )
        )
        # 77891 low
        # 1792222 correct


class Day7_2(Day7_1):
    """
    Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
    """

    def solve(self, input_string: str) -> int:
        root = self.get_graph(input_string)
        space_total = 70000000
        space_needed = 30000000
        space_utilized = root.size
        space_free = space_total - space_utilized
        size_target_min = space_utilized - space_needed
        candidates = list(
            self.filter_nodes(
                lambda node: node.file_type == FileType.directory
                and node.size >= size_target_min,
                root,
            )
        )
        print(
            *list(
                (n.name, n.size)
                for n in sorted(
                    self.filter_nodes(
                        lambda node: node.file_type == FileType.directory,
                        root,
                    ),
                    key=lambda n: n.size,
                    reverse=True,
                )
            )
        )
        chosen = min(candidates, key=lambda n: n.size)
        print(
            chosen.name,
            f"{space_utilized} - {chosen.size} = {space_utilized - chosen.size}. {chosen.name}>= {size_target_min} ({chosen.size>=size_target_min})",
        )
        # 14733871 high
        return chosen
