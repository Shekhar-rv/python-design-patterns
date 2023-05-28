# Dependency Inversion Principle
# High-level modules should not depend on low-level ones; use abstractions
# Abstractions should not depend on details; details should depend on abstractions

from enum import Enum
from abc import abstractmethod
from typing import Tuple, List


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name: str):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name: str):
        pass


class Relationships(RelationshipBrowser):  # low-level
    def __init__(self):
        self.relations: List[str] = []

    def add_parent_and_child(self, parent: str, child: str):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name: str):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # High level module
    # def __init__(self, relationships):
    #     # find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}.')


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    # low-level module
    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)  # type: ignore
    relationships.add_parent_and_child(parent, child2)  # type: ignore
    Research(relationships)
