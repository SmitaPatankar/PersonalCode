# encapsulation
"""
wrap up data members and functions into an entity

data members = properties/state
functions = methods/behavior
capsule = class

fully encapsulated class - all data members private

data hiding - security - private
readonly class - have only getter no setter
reusable code
unit testing becomes manageable
"""

# program: encapsulation
"""
class Student:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    name = property(get_name)
s = Student("smita")
print(s.name)
"""

# inheritance
"""
class properties inherited by another class just like parent and child

eg: parent: human - height, weight, age
eg: child: male, female

parent and child class
super and sub class
"""

# inheritance program
"""
class Human:
    height = 5
    weight = 60
    age = 30
    def get_age(self):
        return self.age
    def set_weight(self, weight):
        self.weight = weight
class Male(Human):
    colour = "white"
    def sleep(self):
        print("male sleeping")
m = Male()
print(m.get_age())
m.set_weight(45)
print(m.weight)
m.sleep()
"""

# todo: python: read inheritance modes public private protected
# modes of inheritance: program
# cpp: protected can be accessed only in child class
"""
class A:
    __a1 = 5
    _a2 = 15
    a3 = 25
class B(A):
    pass
b = B()
print(b._A__a1)
print(b._a2)
print(b.a3)
"""

# todo: implement different types of inheritance in python
# types of inheritance
"""
single - a-->b
multilevel - a-->b-->c eg: animal,dog,pug
multiple - a,b-->c --> eg: speak,bark, speak+bark
hybrid - a-->b a-->c d-->c - combination of more than 1 types of inhyeritance
hierarchical - a-->b,c,d b--> e,f,g, so on... - one class is parent for many
"""

# todo: hw: read about oops: https://www.codingninjas.com/codestudio/guided-paths/basics-of-c/content/118817/offering/1382190: esp: need for types of inheritance

# todo: python: read inheritance ambiguity algorithm
# inheritance ambiguity
"""
class A:
    def m(self):
        print('m in A')
class B:
    def m(self):
        print('m in B')
class C(A, B):
    pass
c = C()
c.m()
"""

# todo: python: read: function overloading(*args, *kwargs), operator overloading(__add__ etc)
# todo: cpp: check why compile time and runtime
# polymorphism
"""
existing in multiple forms

eg: person is brother, father, husband etc

cpp:
compile time or static polymorphism - function overloading(different parameters), operator overloading(+ add,concatenate,print something)
runtime/dynamic polymorphism - method overriding - change inherited method - name and parameters should be same
"""

# operator overloading program
"""
class C:
    def __init__(self, num):
        self.num=num
    def __add__(self, obj):
        return self.num + obj.num
obj1 = C(5)
obj2 = C(10)
print(obj1 + obj2)
"""

# function overloading program
"""
def m(*args, **kwargs):
    print(args)
    print(kwargs)
m(1,2,3,name="smita")
"""

# todo: python: read method overriding
# method overriding
# coz it needs most of the functions from parent but for few has to write its own
"""
class A:
    def m(self, num):
        print(f"m in A {num}")
class B(A):
    def m(self, number):
        print(f"m in B {number}")
b = B()
b.m(5)
"""

# abstraction
"""
implementation hiding

eg: sending email - implementation is hidden - send button is shown

cpp: use access specifiers - so no one else except us can change - security, reusable
"""

# todo: read abstraction python
# abstraction program
"""
from abc import ABC, abstractmethod
class C(ABC):
    def m(self, i, j, k):
        print(f"m -- {i} {j} {k}")
    @abstractmethod
    def mm(self, i, j, k):
        pass
class D(C):
    def mm(self, a, b, c):
        print(f"mm -- {a} {b} {c}")
d = D()
d.m(4,5,6)
d.mm(44,55,66)
"""

# todo: hw: learn: abstraction vs encapsulation: https://stackoverflow.com/questions/742341/difference-between-abstraction-and-encapsulation

# todo: read about interface, virtual function, friend function in cpp and python - https://www.codingninjas.com/codestudio/guided-paths/basics-of-c/content/118817/offering/1382190

# todo: learn more cpp and python oops concepts - https://whimsical.com/object-oriented-programming-cheatsheet-by-love-babbar-YbSgLatbWQ4R5paV7EgqFw
