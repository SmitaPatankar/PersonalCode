from array import *

# create an array of signed integers with 2 bytes size
a = array('i', [1,2,3,4,5])

# traverse
for i in a:
    print(i)

# access
print(a[4])

# append (at end)
a.append(6)
print(a)

# insert (at any point)
a.insert(0,11)
print(a)

# extend
b = array('i', [7,8])
a.extend(b)
print(a)

# add from list
lst = [9,10,11]
a.fromlist(lst)
print(a)

# remove
a.remove(5)
print(a)

# pop - from end
a.pop()
print(a)

# find index
print(a.index(10))

# reverse
a.reverse()
print(a)

# get buffer_info (buffer starts from where in memory and has how many elements)
print(a.buffer_info())

# count
print(a.count(2))

# convert tolist
# print(a.tolist())

# slice
print(a[1:4])
