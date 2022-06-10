# quick sort - https://www.codingninjas.com/codestudio/problems/quick-sort_983625
# begin with whole array i.e. start is 0 and end is length - 1
#
# take starting element i.e. PIVOT
#
# PARTITION the array
#     i.e. count elements smaller than pivot and then put pivot at start+count
#     put all smaller elements to left
#     put all greater elements to right
# return pivot position
#
# RECURSIVELY PARTITION left and right halfs
#
# when start and end is same or crossed i.e. array has 0 or 1 element, it is already sorted so RETURN
#
# for putting smaller or equal elements to left and greater to right
#     put pointers i and j at start and end
#     find greater element at i else keep moving further
#     find smaller or equal element at j else keep moving backwards
#     when both i and j have incorrect elements, swap and move both forward and backward respectively
#     when either pointer reaches pivot, stop as it is already sorted
"""
def partition(a,start,end):
    pivot = a[start]
    print(f"pivot is {pivot}")
    count = 0
    for i in range(start+1,end+1):
        if a[i] <= pivot:
            count += 1
    pivot_index = start+count
    print(f"pivot_index is {pivot_index}")
    a[start], a[pivot_index] = a[pivot_index],a[start]
    i = start
    j = end
    while i < pivot_index and j > pivot_index:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if (i < pivot_index and j > pivot_index):
            a[i], a[j] = a[j],a[i]
            i += 1
            j -= 1
    print(f"partitioned array is {a}")
    return pivot_index
def quick_sort(a,start,end):
    if start >= end:
        return
    p = partition(a, start, end)
    quick_sort(a,start,p-1)
    quick_sort(a,p+1,end)
a = [3,8,0,1,2,10]
n = 6
print(a)
quick_sort(a,0,n-1)
print(a)
"""

# tbd: calculate quick sort with recursion complexities
# quick sort complexity
"""
space - O(n) - for main array itself
time - O(n^2) worst - O(nlogn) best
"""

# hw: check if quick sort is in place
"""
yes, because we are just swapping in place not creating copy for sort
"""

# hw: check if quick sort is stable
"""
No, because place of equal elements is not maintained during swapping and sorting here.
eg:
original:
0  1  2 3 4  5
--------------
1a 2 1b 3 1c 4

0  1  2 3 4  5
--------------
1b 1c 1a 3 2 4
    0  1 
    -----
    1b 1c
        0  1 
        -----
        1b 1c
            0 
            --
            1b
            1 
            --
            1c
    3 4 5
    -------
    3 2 4
        3 4 5
        -------
        2 3 4

            3
            -------
            2
            5
            -------
            4

ans:
0   1   2   3  4   5
-------------------------
1b  1c  1a  2  3   4
"""

# hw: read: https://www.geeksforgeeks.org/quick-sort/: why quick sort over merge sort normally even when it is more time complex?
# todo: learn why is quick sort cache friendly
"""
quick sort's inner loop can be made faster
quick sort can be stopped from hitting worst case by choosing pivot efficiently
quick sort is not in place, but can be made

merge sort is better for large data on external storage
----------------------------------------------------------------------------------
quick sort doesnt need extra space merge sort does for its default implementation
memory allocation and deallocation for merge sort takes extra time

both algos have same complexity on average i.e. O(nlogn)

tail calls can be reduced

is cache friendly
"""

# hw: read: https://www.geeksforgeeks.org/quick-sort/: why quick sort over merge sort for linked lists?
"""
unlike arrays, in linked lists, we can insert elements in middle without extra space
hence merging can be done without extra space

quick sort is not good for linked lists because unlike arrays, random access is not possible and quick sort needs lot of random access.
merge sort is sequential with low random access.
"""

# own: check picking which pivot is best and why
"""
first or last may not be best if already sorted

middle may be ok

median of 3 may be better
move it to first position for further steps
"""

# own: quick sorting partitioning without counting min first
# keep i pointer for where our pivot should lie ultimately, initially at 0
# keep pointer j to find smaller elements than pivot
# whenever j finds smaller,move i forward to make way for smaller element before pivot
# swap i and j
# at the end of j loop, i will be where pivot should ultimately be i.e. on last smallest element
# swap i with 0 i.e. swap last smallest element with pivot
# now we have all smaller elements then pivot then larger
"""
def median(a, start, end):
    mid = start + (end-start)//2
    if a[start] < a[mid]:
        if a[mid] < a[end]:
            return mid
    else:
        if a[start] < a[end]:
            return start
    return mid
def partition(a, start, end):
    pivot_index = median(a, start, end)
    a[start], a[pivot_index] = a[pivot_index], a[start]
    pivot = a[start]
    i = start
    for j in range(start,end+1):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i], a[start] = a[start], a[i]
    print(a)
    return i
def quick_sort(a, start, end):
    if start >= end:
        return
    p = partition(a, start, end)
    quick_sort(a, start, p-1)
    quick_sort(a, p+1, end)
a = [3,4,5,1,2]
print(str(a)+"--------------")
quick_sort(a, 0, 4)
print(str(a)+"--------------")
"""

# todo: 3 way quick sort - https://www.geeksforgeeks.org/quick-sort/ - for redundant elements - all redundant pivots placed once

# todo: quick sort on linked lists singly and doubly - https://www.geeksforgeeks.org/quick-sort/

# todo: quick sort iteratively - https://www.geeksforgeeks.org/quick-sort/

# todo: optimize quick sort with tail call reduction - https://www.geeksforgeeks.org/quick-sort/
"""
while l<h
find p
make 2 parts from l to p-1 and p+1 to h
whichever is smaller process that only
then when we come back, larger will get processed
this way, recursive calls stack is reduced
"""
