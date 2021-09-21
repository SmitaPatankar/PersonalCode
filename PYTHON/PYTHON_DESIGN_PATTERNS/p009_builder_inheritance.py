# multiple builders for object, along with inheritance to follow open close principle

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.dob = None

    def __str__(self):
        return f"{self.name} was born on {self.dob} and works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthdayBuilder(PersonJobBuilder):
    def born(self, dob):
        self.person.dob = dob
        return self


pb = PersonBirthdayBuilder()
me = pb.called("smita").works_as_a("softwareengineer").born("1-1-1980")
