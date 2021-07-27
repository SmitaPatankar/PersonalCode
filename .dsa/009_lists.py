# ordered collection of items
# like shopping list
# different data types
# single or nested

# memory allocation same as array
# LEARN MORE - IS MEMORY ALLOCATION OF LIST SAME AS ARRAY COZ IT HAS TO KNOW DATATYPE ALSO

# create
# time = O(1)
# space = O(n)
l = [1,2,3,4]
print(l)

l = ["abc", "pqr"]
print(l)

l = [1,1.2,"smita"]
print(l)

l = [[1,2,3,4],[1.5,1.6],["a"]]
print(l)

l = []
print(l)

# access
# time = O(1)
# space = O(1)
l = ["milk", "cheese", "butter"]
print(l[0])
print(l[-1])

# traverse and print
# time = O(n)
# space = O(1)
for i in l:
    print(i)

# traverse empty
for i in []:
    print(i)

# traverse and perform operation
for i in range(len(l)):
    l[i] = l[i] + " done"
print(l)

# update
# time = O(1)
# space = O(1)
l = [1,2,3,4,5,6,7]
l[2] = 33
print(l)

# insert - at any location - shift other elements forward
# time = O(n) or O(1) at end
# space = O(1)
l.insert(0, 0)
print(l)

# append at end - direct
# time = O(1)
# space = O(1)
l.append(55)
print(l)

# extend at end with other list elements - one by one
# time = O(n)
# space = O(n)
l.extend([66,77])
print(l)

# slice
print(l[0:2])

# slice - update
l[0:2] = [0.0, 1.1]
print(l)

# pop - from certain location - shift others backwards
# time = O(n)
# space = O(1)
print(l.pop(1))
print(l)

# pop - from end 0 direct
# time = O(1)
# space = O(1)
print(l.pop())
print(l)

# del - from certain location - push others bakcwards
# time = O(n) or O(1) from end
# space = O(1)
del l[3]
print(l)

# del - slice - push others backwards
# time = O(n)
# space = O(1)
del l[3:4]
print(l)

# remove element
# time = O(n)
# space = O(1)
l.remove(2)
print(l)

# search with in
# time = O(n)
def search(a, i):
    if i in a:
        return(l.index(i))
    else:
        return("not found")
print(search(l, 33))

# search linearly
# time = O(n)
# space = O(1)
def search(a, i):
    for e in a:
        if e == i:
            return(l.index(e))
    return("not found")
print(search(l, 33))

# shuffle
import random
l = [1,2,3]
random.shuffle(l)
print(l)
