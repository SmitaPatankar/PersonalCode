# A metaclass is defined by inheriting from type.
# In the default case, a metaclass receives the contents of associated class
# # statements in its __new__ method.
# Here, you can modify the class information before the type is actually constructed:
# unlike inheriting from collections.abc for custom container type

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass

'''
(<class '__main__.Meta'>,
 'MyClass',
 (<class 'object'>,),
 {'__module__': '__main__',
  '__qualname__': 'MyClass',
  'foo': <function MyClass.foo at 0x102c7dd08>,
  'stuff': 123})
'''

# Python 2
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        pass  # ...
class MyClassInPython2(object):
    __metaclass__ = Meta
    # ...

class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Don't validate the abstract Polygon class
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # Specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Triangle(Polygon):
    sides = 3

print('Before class')
class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')
print('After class')

print('Before class')
class Line(Polygon):
    print('Before sides')
    sides = 1
    print('After sides')
print('After class')

'''
Before class
Before sides
After sides
Traceback ...
ValueError: Polygons need 3+ sides
'''

# The __new__ method of metaclasses is run after the class statement’s entire body has been processed.
