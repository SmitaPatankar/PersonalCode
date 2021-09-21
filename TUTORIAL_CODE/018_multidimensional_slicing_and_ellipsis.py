# a[m:n, k:l] for 2d numpy.ndarray
# the [] operator simply receive the indices in a[i, j] as a tuple
# i.e. to evaluate a[i, j], Python calls a.__getitem__((i, j))
'''
NumPy uses ... as a shortcut when slicing arrays of many dimensions
if x is a four-dimensional array, x[i, ...] is a shortcut for x[i, :, :, :,].
'''

# they can also be used to change mutable sequences in place

