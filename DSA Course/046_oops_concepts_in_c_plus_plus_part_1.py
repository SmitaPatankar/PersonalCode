# 4 pillars of object oriented programming
"""
inheritance
encapsulation
polymorphism
abstraction
"""

# object oriented programming
"""
revolves around object
"""

# object
"""
entity that has:

state/property
behavior

eg: camera, phone etc

eg: game hero
properties - name, health, life
behavior - attack, defense
"""

# why oop
"""
make it close to real world to make it more readable, maintainable and extensible
"""

# class
"""
type for object

eg: int a, str b
eg: Hero Paul

i.e. user defined data type/custom data type

object is instance of class

class is like a template or blueprint
"""

# todo: check how size of user defined data type is determined in python
# oop program
# in cpp size of object is 4 bytes if it has one integer value in it
# in cpp size of empty class object is 1 for tracking
"""
class Hero:
    def __init__(self, health):
        self.health = health
h1 = Hero(1)
"""

# import program
# access object properties using .
"""
hero = __import__('046_hero')
h1 = hero.Hero("paul",1,2)
print(h1.name)
print(h1.health)
print(h1.level)
"""

# access modifiers
"""
where can the properties of behavior of an object be accessed from

private - only in class eg: functions in class - python start with __
protected - only in class and child class - python start with _
public - within and outside class eg: reading and writing to object - by default in python
"""

# access modifiers program
"""
class Hero:
    def __init__(self, name, health, level):
        self.__name = name
        self._health = health
        self.level = level
h1 = Hero("paul",1,2)
print(h1._Hero__name)  # private works outside with class name mangling in python
print(h1._health)  # protected works outside as it is
print(h1.level)  # public anyways works anywhere
h1.name = "Smita"
"""

# set values
"""
h1.level = 5
print(h1.level)
"""

# getters and setters for private variables
# can use conditions too
""""
class Hero:
    def __init__(self, name):
        self.__name= name
    def set_name(self, name):
        if name == "smita":
            self.__name = name
        else:
            raise ValueError("name should be smita")
    def get_name(self):
        return self.__name
    def del_name(self):
        del self.__name
    name = property(get_name, set_name, del_name)
h = Hero("smita")
print(h.name)
try:
    h.name = "neha"
except Exception as e:
    print(e)
print(h.name)
del h
"""

# padding in cpp or alignment in cpp
# object with one int and one char takes takes 8 bytes instead of 4 + 1 i.e. 5 bytes
# because 32 bits system reads data in chunks of 4 bytes
# so char has 3 bytes as padding
# similarly 8 bytes for 64 bit system
# i.e. bits divide by 4
# hence arrange elements in such a sequence that memory is not wasted
# eg:
# int 4 + 4 for padding
# double 8
# char 1 + 7 for padding
# i.e. 24 bytes
# eg: double 8
# int 4
# char 1 + 3 padding
# i.e. 16 bytes
# 32 bit system can read 32 bits in one go
# i.e 32/8 = 4 i.e. 4 bytes
# 64 bit system can read 64 bits in one go
# i.e. 64/8 = 8 bytes

# todo: hw: cpp: greedy alignment

# in cpp pointer can also be made for a new class object

# object creation
# todo: read python __new__ parameters and return type
"""
constructor gets called
created by default
__new__() in python
"""

# self keyword
# self is a pointer i.e. saves address of where our current object is actually stored
# init stores value passed to function in actual object
# init is called by default without any parameters after object is created
# we can create our own parameterized init
"""
class Hero:
    def __init__(self, name):
        print(id(self))
        print(self)
        self.name = name
h = Hero("smita")
print(id(h))
print(h)
print(h.name)
"""

# cpp has copy constructor where instead of individual values for initialization, another object is passed by reference

# copy
# shallow copy - same memory gets accessed by 2 diff names for array
# deep copy - different memory gets accessed by 2 diff names for array
# both copies - same memory is accessed for immutable objects in python
"""
import copy
class Hero:
    def __init__(self, arr, s):
        self.arr = arr
        self.s = s
h1 = Hero([1,2,3], "abc")
h2 = copy.copy(h1)
h3 = copy.deepcopy(h1)
print(f"h1 array {id(h1.arr)} {h1.arr} h2 {id(h2.arr)} {h2.arr} h3 {id(h3.arr)} {h3.arr}")
print(f"h1 string {id(h1.s)} {h1.s} h2 {id(h2.s)} {h2.s} h3 {id(h3.s)} {h3.s}")
h1.arr[0] = 11
h1.s = "abcabc"
print(f"h1 array {id(h1.arr)} {h1.arr} h2 {id(h2.arr)} {h2.arr} h3 {id(h3.arr)} {h3.arr}")
print(f"h1 string {id(h1.s)} {h1.s} h2 {id(h2.s)} {h2.s} h3 {id(h3.s)} {h3.s}")
"""

# todo: hw: cpp: read about oops: https://www.codingninjas.com/codestudio/guided-paths/basics-of-c/content/118817/offering/1382190

# copy assignment operator
# both are one and the same object
"""
class Hero:
    def __init__(self, names):
        self.names = names
h1 = Hero([1,2,3])
h2 = Hero([4,5,6])
print(f"h1 id {id(h1)} h2 id {id(h2)} h1 names id {id(h1.names)} h1 names {h1.names} h2 names id {id(h2.names)} h2 names {h2.names}")
h1 = h2
print(f"h1 id {id(h1)} h2 id {id(h2)} h1 names id {id(h1.names)} h1 names {h1.names} h2 names id {id(h2.names)} h2 names {h2.names}")
h1.names[0] = 11
print(f"h1 id {id(h1)} h2 id {id(h2)} h1 names id {id(h1.names)} h1 names {h1.names} h2 names id {id(h2.names)} h2 names {h2.names}")
"""

# todo: python: learn more about garbage collection, how often it occurs
# destructor
# deallocate memory
# gets called when object is about to die or go out of scope
# eg: at the end of function which defined it
# python has __del__() for the same
"""
class Hero:
    def __init(self):
        print("initializing")
    def __del__(self):
        print("deleting")
def main():
    h = Hero()
    print(h)
    print("blah")
main()
"""

# todo: cpp: constants - use with objects and functions
# constants in cpp - in python define in capitals but that is just namesake

# todo: python: check how args are diff from just passing a list
# todo: hw: cpp : initializer list
# cpp initializer list - as many args
"""
def m(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(m(1,2,3,4,5))
"""

# todo: python check why static functions are not written outside
# static keyword
# belongs to the class
# no need to create object
# but can be accessed from object also but not recommended
# when we assign to object to that variable, it is actually instance variable
# can access static members
"""
class Hero:
    x = 5  # static variable
    @staticmethod
    def m():  # static function  # doesnt use self or cls
        print("m")
print(Hero.x)
Hero.m()
h = Hero()
print(h.x)
h.m()
Hero.x = 10
print(h.x)
"""
