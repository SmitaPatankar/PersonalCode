# metaclass defines rules for a class
# type is a metaclass

class Test:
    pass


def func():
    pass


print("type class")
print(type)
print()

print("class")
print(Test)
print("type of class")
print(type(Test))
print()

print("object")
print(Test())
print("type of object")
print(type(Test()))
print()

print("type of int object")
print(type(2))
print()

print("func")
print(func)
print("type of func")
print(type(func))
print()

# ########################################


class Foo:
    def show(self):
        return("hi")


def add_attribute(self):
    self.z = 9


Test = type("Test", (Foo,), {"x":5, "add_attribute": add_attribute})
t = Test()
print(t.show())
print(t.x)
t.add_attribute()
print(t.z)
print()

# ########################################


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        a = {}
        for k, v in attrs.items():
            if k.startswith("__"):
                a[k] = v
            else:
                a[k.upper()] = v
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        return "hi"


d = Dog()
print(d.X)
print(d.Y)
print(d.HELLO())
