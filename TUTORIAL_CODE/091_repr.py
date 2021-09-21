print('foo bar')
>>>
foo bar

# human readable form

print('%s' % 'foo bar')
>>>
foo bar

we dont know type

print(5)
print('5')

>>>
5
5

hence repr

a = '\x07'
print(repr(a))

>>>
'\x07'

b = eval(repr(a))
assert a == b
# original value

print(repr(5))
print(repr('5'))

>>>
5
'5'

print('%r' % 5)
print('%r' % '5')

>>>
5
'5'

class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 2)
print(obj)

>>>
<__main__.OpaqueClass object at 0x107880ba8>

class BetterClass(object):
    def __init__(self, x, y):
        # ...

    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)

obj = BetterClass(1, 2)
print(obj)

>>>
BetterClass(1, 2)

# if you dont control class

obj = OpaqueClass(4, 5)
print(obj.__dict__)

>>>
{'y': 5, 'x': 4}

