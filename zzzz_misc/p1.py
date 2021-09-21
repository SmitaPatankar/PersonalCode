from copy import deepcopy, copy

l = [1,2,3,[4,5,6]]
scopy = copy(l)
dcopy = deepcopy(l)

# scopy[3][0] = 44
dcopy[3][0] = 44

print(l)
print(scopy)
print(dcopy)
