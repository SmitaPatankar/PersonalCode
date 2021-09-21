'''
Meanwhile, if you are doing advanced numeric processing in arrays, you should be using the NumPy and SciPy libraries.

NumPy implements multi-dimensional, homogeneous arrays and matrix types that hold not only numbers but also user-defined records, and provides efficient elementwise operations.

SciPy is a library, written on top of NumPy, offering many scientific computing algorithms from linear algebra, numerical calculus, and statistics.
'''

import numpy
a = numpy.arange(12)
print(a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(type(a))
# <class 'numpy.ndarray'>
print(a.shape)
# (12,)
a.shape = 3, 4
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(a[2])
# [ 8  9 10 11]
print(a[2, 1])
# 9
print(a[:, 1])
# [1 5 9]
print(a.transpose())
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

# need to install numpy



print("##########################")

import numpy
floats = numpy.loadtxt('floats-10M-lines.txt')
print(floats[-3:])
# [ 3016362.69195522,   535281.10514262,  4566560.44373946])
floats *= .5
print(floats[-3:])
# array([ 1508181.34597761,   267640.55257131,  2283280.22186973])

from time import perf_counter as pc
t0 = pc(); floats /= 3; pc() - t0
# 0.03690556302899495
numpy.save('floats-10M', floats)
floats2 = numpy.load('floats-10M.npy', 'r+')
floats2 *= 6
print(floats2[-3:])
# memmap([ 3016362.69195522,   535281.10514262,  4566560.44373946])

# $ sudo apt-get install python-numpy python-scipy

