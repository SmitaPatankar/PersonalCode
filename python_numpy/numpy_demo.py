# theory
"""
for scientific computing
base of pandas
for single or multi dimensional arrays
faster than lists because it has fixed types i.e. int saved as int32 i.e. 4 bytes or we can reduce to 16 i.e. 2 bytes or 8 i.e. 1 byte also
lists have object value(8 bytes), object type(4 bytes), reference count(8 bytes), size(8 bytes) of int value
hence numpy is faster to read
type checking is not needed while iterating over numpy
numpy uses contiguous memory unlike lists
single instruction multiple data - all additions at a time
cache utilization
numpy has more operations
useful in plotting
for machine learning
refer docs
"""

# installation
"""
pip install numpy
"""

# import
import numpy as np

# create and print array
d = np.array([1, 2, 3])
print(d)
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]], dtype="int16")
print(a)
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
print(np.zeros([5, 4]))
print(np.ones([5, 4], dtype="int32"))
print(np.full((2, 2), 99))
print(np.full((2, 2), 99, dtype="float32"))
print(np.full_like(a, 4))
print(np.random.rand(4, 2))
print(np.random.randn(4,4))
print(np.random.random_sample(a.shape))
print(np.random.randint(7, size=(3, 3)))
print(np.random.randint(-4, 8, size=(3, 3)))
i = np.identity(5)
print(i)
print(np.repeat(a, 3))
print(np.repeat(a, 3, axis=0))
data = np.genfromtxt("data.txt", delimiter=",")
print(data)
print(np.arange(25))
print(np.arange(start=0,stop=10))
print(np.arange(start=0,stop=11, step=2))
print(np.linspace(start=0, stop=100, num=5))
print(np.eye(4))

# describe array
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)

# print parts of array
print(a[1, 5])
print(a[1, -2])
print(a[0, :])
print(a[:, 2])
print(a[0, 1:6:2])
print(a[0, 1:-1:2])
print(b[0, 1, 1])
print(d[[0, 1]])

# update array values
a[1, 5] = 20
print(a)
a[:, 2] = 5
print(a)
a[:, 2] = [1, 2]
print(a)
b[:, 1, :] = [[9, 9],[8, 8]]
print(b)

# update type of array
print(data.astype("int32"))

# update shape of array
print(a.reshape(7, 2))

# copy array
c = a.copy()
c[0] = 100
print(c)
print(a)

# array operations
print(d)
print(d+2)
print(d-2)
print(d*2)
print(d**2)
print(np.sin(d))
print(np.cos(d))
print(d+d)
print(np.matmul(d, d))
print(np.linalg.det(i))

# array aggregate operations
print(np.min(a))
print(np.max(a))
print(a.argmax())  # index
print(np.min(a, axis=1))
print(np.sum(a))
print(np.sum(a, axis=1))
print(np.sqrt(a))

# stack arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack([a, b, b]))
print(np.hstack([a, b, b]))

# array comparison operations
print(a > 1)
print(a[a > 1])
print(np.any(a > 2))
print(np.all(a > 0))
print((a > 2) & (a < 5))
print(~((a > 2) & (a < 5)))
