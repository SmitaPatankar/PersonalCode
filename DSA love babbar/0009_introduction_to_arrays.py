# array
"""
- list of similar type of items in one data structure
- eg: int, bool, string, custom class objects etc
- items stored in contiguous memory locations
- eg: 3  |5  |9  |2  |11   --> value
      0  |1  |2  |3  |4    --> index
      100|104|108|112|116  --> memory location
- access elements via index
- array stores actual memory location of first object
- array also stores its length
"""

# array operations program
"""
# create array with one element
a = [15]
# access an element
print(a[0])
# create array with multiple elements
b = [5, 7, 11]
# access an element
print(b[2])
# access all elements one by one
n = 3
for i in range(3):
    print(b[i])
# create array with multiple same elements - homework
c = [1] * 10
print(c)
"""

# array access program via function
"""
def print_array(a, size):
    for i in range(size):
        print(a[i])
d = [1,2,3]
print_array(d, 3)
"""

# array size program
"""
import sys
e = []
print(sys.getsizeof(e))  # 56 - 0 elements
e = [1]
print(sys.getsizeof(e))  # 64 - 1 element
e = [1, 2]
print(sys.getsizeof(e))  # 72 - 2 elements
e = [1, 2, 3]
print(sys.getsizeof(e))  # 120 - 3 elements (80)
e = [1, 2, 3, 4]
print(sys.getsizeof(e))  # 120 - 4 elements (88)
e = [1, 2, 3, 4, 5]
print(sys.getsizeof(e))  # 120 - 5 elements (96)
e = [1, 2, 3, 4, 5, 6]
print(sys.getsizeof(e))  # 120 - 6 elements (104)
e = [1, 2, 3, 4, 5, 6, 7]
print(sys.getsizeof(e))  # 120 - 7 elements (112)
e = [1, 2, 3, 4, 5, 6, 7, 8]
print(sys.getsizeof(e))  # 120 - 8 elements (120)
e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sys.getsizeof(e))  # 152 - 9 elements (128)
"""

# array length program
"""
f = [1, 2, 3]
print(len(f))
"""

# array of strings program
"""
# create
strarray = ["a", "b", "c"]
# access one element
print(strarray[2])
# access all elements via function
def print_array(a, size):
    for i in range(size):
        print(a[i])
print_array(strarray, 3)
"""

# array max and min element program
"""
def get_max(num, n):
    maxi = 0 - (2**31)
    for i in range(n):
        # if num[i] > maxi:
        #     maxi = num[i]
        maxi = max(maxi, num[i])
    return maxi
def get_min(num, n):
    mini = (2**31) - 1
    for i in range(n):
        # if num[i] < mini:
        #     mini = num[i]
        mini = min(mini, num[i])
    return mini
def main():
    size = int(input("enter array size "))
    a = []
    for i in range(size):
        a.append(int(input("enter an array element "))
    print(f"max is {get_max(a, size)}")
    print(f"min is {get_min(a, size)}")
main()
"""

# scope of array program
"""
def update(a, n):
    print("inside", end=" ")
    a[0] = 11
    for i in range(n):
        print(a[i], end=" ")
    print("going back")
def main():
    a = [1, 2, 3]
    update(a, 3)
    for i in range(3):
        print(a[i], end=" ")
main()
"""

# homework
# print sum of all elements in array
# input size
# input elements
# output sum
"""
def sum(a, size):
    sum = 0
    for i in range(size):
        sum += a[i]
    return sum
def main():
    size = int(input("enter size "))
    a = []
    for i in range(size):
        a.append(int(input("enter an element "))
    print(sum(a, size))
main()
"""

# array linear search program
"""
def search(a, size, key):
    for i in range(size):
        if a[i] == key:
            return True
    return False
def main():
    a = [1, 2, 10, 8, 3, 4, -1, 9, 100, 10]
    key = int(input("enter key "))
    found = search(a, 10, key)
    if found:
        print("is present")
    else:
        print("is not present")
main()
"""

# reverse an array program
# swap elements from left most and right most and then move left pointer forward and right one backward
"""
def reverse(a, size):
    start = 0
    end = size - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
def print_array(a, size):
    for i in range(size):
        print(a[i], end=" ")
    print()
def main():
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 4, 5]
    reverse(a, 6)
    reverse(b, 5)
    print_array(a, 6)
    print_array(b, 5)
main()
"""
