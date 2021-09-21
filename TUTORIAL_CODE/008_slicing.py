a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
# First four: ['a', 'b', 'c', 'd']
print('Last four: ', a[-4:])
# Last four:  ['e', 'f', 'g', 'h']
print('Middle two:', a[3:-3])
# Middle two: ['d', 'e']

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

print("##########")

print(a[:])      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[:5])     # ['a', 'b', 'c', 'd', 'e']
print(a[:-1])    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a[4:])     #                     ['e', 'f', 'g', 'h']
print(a[-3:])    #                          ['f', 'g', 'h']
print(a[2:5])    #           ['c', 'd', 'e']
print(a[2:-1])   #           ['c', 'd', 'e', 'f', 'g']
print(a[-3:-1])  #                          ['f', 'g']

# print(a[20])
# IndexError: list index out of range

first_twenty_items = a[:20]
last_twenty_items = a[-20:]

print("##########")

b = a[4:]
print('Before:   ', b)  # Before:    ['e', 'f', 'g', 'h']
b[1] = 99
print('After:    ', b)  # After:     ['e', 99, 'g', 'h']
print('No change:', a)  # No change: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("##########")

print('Before ', a)  # Before  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[2:7] = [99, 22, 14]
print('After  ', a)  # After   ['a', 'b', 99, 22, 14, 'h']

print("##########")

# copy is made
b = a[:]
assert b == a and b is not a

b = a
print('Before', a)  # Before ['a', 'b', 99, 22, 14, 'h']
a[:] = [101, 102, 103]
assert a is b
print('After ', a)      # After  [101, 102, 103]
