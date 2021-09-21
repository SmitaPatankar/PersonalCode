'''
If the list will only contain numbers, an array.array is more efficient than a list: it supports all mutable sequence operations (including .pop, .insert, and .extend), and additional methods for fast loading and saving such as .frombytes and .tofile.

When creating an array, you provide a typecode, a letter to determine the underlying C type used to store each item in the array. For example, b is the typecode for signed char. If you create an array('b'), then each item will be stored in a single byte and interpreted as an integer from –128 to 127. For large sequences of numbers, this saves a lot of memory. And Python will not let you put any number that does not match the type for the array.
'''

from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
# 0.07802343889111107

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
# 0.07802343889111107
print(floats2 == floats)
# True

# d - double-precision floats
# tofile fromfile - speedy and smalle file

'''
list and array.array

s.__add__(s2) - s + s2
s.__iadd__(s2) - s += s2
s.append(a)
s.__contains__(e) - e in s
s.count(e)
s.__delitem__(p)
s.extend(it)
s.__getitem__(p) - s[p]
s.index(e)
s.insert(p,e)
s.__iter__()
s.__len__() - len(s)
s.__mul__(n) - s*n - repeated concatenation
s.__imul__(n) - s *= n—in-place repeated concatenation
s.__rmul__(n) - n * s—reversed repeated concatenation
s.pop([p]) - Remove and return item at position p (default: last)
s.remove(e) - Remove first occurrence of element e by value
s.reverse()
s.__setitem__(p, e) - s[p] = e

array.array only
s.byteswap()
s.__copy__()
s.__deepcopy__()
s.itemsize
s.frombytes(e)
s.fromfile(f, n)
s.fromlist(l) - if one causes typeerror none are appended
s.tobytes()
s.tofile(f)
s.tolist()
s.typecode

list only
s.clear()
s.copy()
s.__reversed__()
s.sort([key], [reverse])
'''

# a = array.array(a.typecode, sorted(a))
# no sort function

# To keep a sorted array sorted while adding items to it, use the bisect.insort function

