'''
The built-in memorview class is a shared-memory sequence type that lets you handle slices of arrays without copying bytes.
'''

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
# 5
print(memv[0])
# -2
memv_oct = memv.cast('B')
print(memv_oct.tolist())
# [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4
print(numbers)
# array('h', [-2, -1, 1024, 1, 2])

# short signed integers (typecode 'h')
# typecode 'B' (unsigned char)

# Note change to numbers: a 4 in the most significant byte of a 2-byte unsigned integer is 1024.

