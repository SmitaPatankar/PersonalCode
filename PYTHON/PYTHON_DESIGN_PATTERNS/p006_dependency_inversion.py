# high level modules should depend on abstractions, not low level modules

from abc import ABC, abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 1
    CHILD = 1
    SIBLING = 1


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # low level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high level
    def __init__(self, relationshipbrowser):
        for p in relationshipbrowser.find_all_children_of("John"):
            print(f"John has a child {p}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

r = Research(relationships)
