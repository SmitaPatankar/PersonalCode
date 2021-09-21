from unittest import TestCase


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


pf = PersonFactory()

p1 = pf.create_person('Chris')
print(p1.name)
print(p1.id)

p2 = pf.create_person('Sarah')
print(p2.name)
print(p2.id)
