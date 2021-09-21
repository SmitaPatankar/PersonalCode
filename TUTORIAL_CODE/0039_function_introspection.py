def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

dir(factorial)

'''
['__annotations__', '__call__', '__class__', '__closure__', '__code__',
'__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__get__', '__getattribute__', '__globals__',
'__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__',
'__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__']
'''


def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()


upper_case_name.short_description = 'Customer name'

class C:
    pass
obj = C()
def func():
    pass
print(sorted(set(dir(func)) - set(dir(obj))))
# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
