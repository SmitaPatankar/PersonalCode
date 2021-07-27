# time = O(1)
# space = O(r*c)

# eg: temperature of days
# day1 - 10 30 20
# day2 - 90 80 40

import numpy as np

# create
# time = O(1)
# space = O(mn)
a = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(a)

# insert row - shift other rows down
# time = O(mn) or O(1) for at end
# space = O(1)
b = np.insert(a, 0, [[1,2,3,4]], axis=0)
print(b)

# insert column - shift other columns to right
# time = O(mn) or O(1) for at end
# space = O(1)
c = np.insert(a, 0, [[1,2,3,4]], axis=1)
print(c)

# append row - at end
# time = O(1)
# space = O(1)
d = np.append(a, [[1,2,3,4]], axis=0)
print(d)

# append column - at end
# time = O(1)
# space = O(1)
e = np.append(a, [[1],[2],[3],[4]], axis=1)
print(e)

# access element
# time = O(1)
# space = O(1)
def access(a, i, j):
    if i >= len(a) and j >= len(a[0]):
        print("wrong")
    else:
       print(a[i][j])
access(a, 0, 1)

# traverse
# time = O(mn)
# space = O(1)
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j])

# search
# time = O(mn)
# space = O(1)
def search(a, s):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == s:
                return (i,j)
    return("not found")
print(search(a, 5))

print(a)

# delete row - move other columns upwards
# time = O(mn)
# space = O(1)
b = np.delete(a, 0, axis=0)
print(b)

# delete column - move other columns backwards
# time = O(mn) or O(1) if at end
# space = O(1)
c = np.delete(a, 0, axis=1)
print(c)
