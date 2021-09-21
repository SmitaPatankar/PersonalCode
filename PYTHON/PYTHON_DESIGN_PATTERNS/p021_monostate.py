# make new instances that refer shared state

class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CEO(Monostate):
    def __init__(self):
        self.name = "steve"
        self.age = 55

    def __str__(self):
        return f"{self.name} - {self.age}"


c1 = CEO()

c2 = CEO()
c2.age = 60

print(c1)
print(c2)
