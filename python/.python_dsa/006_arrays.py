# create array
# time = O(1)
# space = O(n)
from array import *
a = array("i", [1,2,3,4,5,6])
b = array("d", [1.3, 4.5])
print(a)
print(b)

# insert into array (shift others to right unless its the last element - copy to larger array if slots are full)
# time=O(1) or O(n)
# space=O(1)
a.insert(6,7)
print(a)
a.insert(0, 0)
print(a)
a.insert(2, 9)
print(a)

# traverse
# time = O(n)
# space = O(1)
for i in a:
    print(i)

# access an element
# time = O(1)
# space = O(1)
def access(arr, i):
    if i >= len(arr):
        print("wrong")
    return arr[i]
print(a[1])

# search an element in unsorted array
# time = O(n)
# space = O(1)
def search(a, element):
    for i in a:
        if element == i:
            return a.index(i)
    return("not found")
print(search([1,2,3,4,5], 5))

# delete an element (delete and move rest of the elements backwards unless its the last element)
# time = O(1) or O(n)
# space = O(1)
a.remove(5)
print(a)
