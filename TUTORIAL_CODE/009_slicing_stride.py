a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)  # ['red', 'yellow', 'blue']
print(evens)  # ['orange', 'green', 'purple']

x = b'mongoose'
y = x[::-1]
print(y)  # b'esoognom'

w = 'Image'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')

w = 'Image'  # weird chars
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])      # ['a', 'c', 'e', 'g']
print(a[::-2])     # ['h', 'f', 'd', 'b']
print(a[2::2])     # ['c', 'e', 'g']
print(a[-2::-2])   # ['g', 'e', 'c', 'a']
print(a[-2:2:-2])  # ['g', 'e']
print(a[2:2:-2])   # []
