# axis
"""
0 = down
1 = across

[[1,2,3]
 [4,5,6]]

sum - 5,7,9
sum - 6, 15

x y
1 3
2 4
3 5
4 6
5 7

mean - 3,5
mean - 2,3,4,5,6
"""

"""
import numpy as np

# create
a = np.array([1, 2, 3], dtype="int16")  # int
b = np.array([1.0, 2.0, 3.0], [1.0, 2.0, 3.0])  # float  # 2d
c = np.zeros(5)  # zeros
d = np.zeros((2, 3, 3))  # zeros  # 2d
e = np.ones((4, 2, 2), dtype="int32")  # ones
f = np.full((2, 2), 99, dtype="float32")  # some num
g = np.full_like(f, 100)  # some num and shape of other
h = np.random.rand(1, 2)  # random
i = np.random.random_sample(a.shape)  # random sample
j = np.random.randint(-4, 7, size=(3, 3))  # random int
k = np.identity(3)  # identity matrix
l = np.repeat(np.array([[1, 2, 3]]), 3, axis=0)  # repeat
m = l.copy()

# describe
print(a.ndim)  # dimensions
print(a.shape)  # row by column
print(a.dtype)  # data type
print(a.itemsize)  # size of each item
print(a.size)  # no of items
print(a.nbytes)  # total bytes of array

a = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]

# view
print(a[0, :])  # row
print(a[:, 2])  # column
print(a[1][5])  # row and column  # negative also
print(a[0:5, 0:5:2])  # rows and columns

# modify
a[1][5] = 20
a[:, 2] = 5
a[:, 2] = [1, 2]

# operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5])
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a ** 2)
print(np.sin(a))
print(np.cos(a))
print(a + b)

# linear algebra
a = np.ones((2,3))
b = np.full((3,2),2)
np.matmul(a,b)

# statistics
a = np.array([1,2,3],[4,5,6])
print(np.min(a))
print(np.max(a, axis=1))
print(np.sum(a, axis=1))

# reorganize
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)
a.reshape((8,1))
print(a.shape)

# stack vertically/horizontally
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
np.vstack([v1, v2])
np.hstack([v1,v2])

# misc
fd = np.genfromtxt("data.txt", ",")
fd.astype("int32")

# adv indexing and boolean masking
print(fd > 5)
print(fd[fd > 50])
print(fd[[1,2,4]])
print(np.any((fd > 50) & (fd < 100), axis=0))  # all  # ~
"""