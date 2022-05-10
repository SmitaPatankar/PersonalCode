# insertion sort details
"""
take each element and INSERT it in correct position

like cards given to us one by one to insert in our hand in sorted order
insert first one directly
from next onwards, insert it in correct order

eg: 13452678 --> 12345678
"""

# todo: try using for loop (gives issue in python)
# hw: program: insertion sort program: while loop
# hw: program: https://www.codingninjas.com/codestudio/problems/insertion-sort_3155179: while loop
# logic: start from index 1 because 0th element is needed as it is in beginning for comparison
# when swap is needed from right to left, put elements between initial position and final position forward by one to make one empty space
# comparison is to be done with all elements before it from right to left until we keep finding greater elements and then put in left of last great element by making empty space by pushing others forward
# if greater, keep in right only
# shift, dont swap
"""
def insertion_sort(a):
    i = 1
    while i < len(a):
        temp = a[i]
        j = i-1
        while j >= 0:
            if temp < a[j]:
                a[j+1] = a[j]
            else:
                break
            j -= 1
        a[j+1] = temp
        i += 1
a = [10,9,8,1,2,3,6,5,4,7]
print(a)
insertion_sort(a)
print(a)
"""

# why insertion sort?
"""
adaptable algorithm
getting sorted with time

beneficial for smaller arrays

if array is already partially sorted
"""

# insertion sort complexities
"""
space - O(1)
time - first time 1 comparison, 2nd time 2 i.e. 1 to n-1 almost i.e. n(n+1)/2 i.e. O(n^2)
best case time - O(n) one comparison for each round i.e. n-1 comparisons
worst case - reverse sorted - O(n^2)
"""

# hw: learn more about adaptable algorithm
"""
adaptable algorithms - identifies within 1 pass i.e. O(n) that the array is already sorted - eg: insertion sort, bubble sort
non adaptable algorithms - keeps performing entire comparisons even if the array was already sorted - eg: selection sort
"""

# hw: learn more about stable algorithm
"""
stable algorithm is when duplicate elements maintain their sequence even after sorting
insertion sort is stable coz it always moves element backwards only is it is smaller so equal elements would maintain order
eg: 1 3* 4 5 6 3# 7
1 3* 3# 4 5 6 7
bubble sort is also stable
selection sort is unstable
"""