def find_third_largest(lst):
    largest = 0
    second_largest = 0
    third_largest = 0
    for element in lst:
        if element > largest:
            third_largest = second_largest
            second_largest = largest
            largest = element
        elif element > second_largest:
            third_largest = second_largest
            second_largest = element
        elif element > third_largest:
            third_largest = element
    return third_largest

list1 = [100, 21, -1, 43, 0, 4332, 654, -64, 994, 66454, 8, 10, -12, 6539, 774382, -540, -64, 921, 19]
print(find_third_largest(list1))

# a.py
# a = 10

import a
output = a.a
