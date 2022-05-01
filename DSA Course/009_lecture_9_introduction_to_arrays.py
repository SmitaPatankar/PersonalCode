# todo: python: how many memory blocks are created for array initially
# todo: python: whether initial memory blocks in array are blank or contain random value
# array details
"""
- list of same type of elements i.e. predefined or custom data types(our class object) in single variable
- values stored in contiguous memory locations
- values have index for access
- eg:
values  -    a  b   c   d
index   -    0  1   2   3
address -   100 104 108 116
- indexes of array are from 0 to length - 1
- array denotes address of first memory block in it, amongst all its memory blocks
-eg:
array[0] points to initial location
array[2] points to initial location + (2 * element size) i.e. 4 bytes for array
- access elements for valid indexes only
"""

# program: array of multiple same values
"""
a = ["*"] * 5
print(a)  # ['*', '*', '*', '*', '*']
"""

# program: array
"""
a = []
print(a)
b = [5, 7, 11]
print(b)
print(b[2])
for i in range(0, len(b)):
    print(b[i])
"""

# program: array with function
"""
def print_array(arr, size):
    for i in range(size):
        print(arr[i])
a = [1,2,3,4,5]
print_array(a, 5)
"""

# todo: python: memory allocation for array elements
# program: array size
"""
print([].__sizeof__())  # 40
print([1].__sizeof__())  # 48
print([1,2].__sizeof__())  # 56
print([1,2,3].__sizeof__())  # 104
"""

# program: array length
"""
print(len([1]))
"""

# program: character array
"""
a = ["a", "b", "c"]
print(a)
print(a[0])
"""

# program: array for max and min element
# logic: initially keep min as int_max and max as int_min and then compare with each element and keep updatingand return
"""
def get_max(a):
    max = (0 - pow(2,31))
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max
def get_min(a):
    min = pow(2,31) - 1
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min
size = int(input("enter size "))
a = []
for i in range(size):
    a.append(int(input(f"enter element number {i}")))
print(get_min(a))
print(get_max(a))
"""

# program: builtin min max functions
"""
print(min(1,2))
print(max(1,2))
"""

# todo: python: pass by value and reference
# program: scope of array
# logic: don't update arrays in functions where they are sent
"""
def update_array(a):
    print("inside function")
    a[0] = 11
    print(a)
    print("going back to main")
a = [1,2,3]
update_array(a)
print(a)  # updated as array's first element address was given to function
"""

# hw: input size and array elements - give sum of array
"""
def sum(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum
size = int(input("enter size "))
a = []
for i in range(size):
    a.append(int(input(f"enter element number {i}")))
print(sum(a))
"""

# program: show if number is power of 2
# logic: if no of set its is one, it can be represented as power of 2
"""
n = 6
set_bit_count = 0
while n != 0:
    bit = n & 1
    n = n >> 1
    if bit == 1:
        set_bit_count += 1
    if set_bit_count > 1:
        break
if set_bit_count == 1:
    print("can be represented as power of 2")
else:
    print("cant be represented as power of 2")
"""

# program: linear search - check if given element is present in array linearly
"""
def search(a, n):
    for i in range(len(a)):
        if n in a:
            return True
    return False
a = [5,7,-2,-1,22,-2,0,5,22,1]
n = 10
print(search(a, n))
"""

# program: reverse array
# logic: while start < end, swap their values, move start forward and move end backwards
# logic: works for both odd and even as anyways center element for odd number stays in its place
"""
a = [1, 2, 3, 4, 5]
start = 0
end = len(a) - 1
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
print(a)
"""
