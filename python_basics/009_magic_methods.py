"""
emulate builtin behavior

__init__ - assigning values to attributes
__add__ - adding 2 integers or appending two strings - similarly __sub__, __mul__, __gt__, __ge__, __lt__, __le__
eg: int.__add__(1,2)
eg: str.__add__("s", "p")
returns NotImplemented when one object doesn't know how to handle it, so that it goes to other object
__repr__ - for repr for developers - for fall back of str for users
__str__ - for str for users
__len__ - for length of string
eg: "smita".__len__()
"""