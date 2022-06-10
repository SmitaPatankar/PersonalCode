# hw: check why
# merge sort time complexity
"""
O(nlogn)
eg: 8 divided into 44, 2222,11111111 -on all 3 levels 8 operations are taken and levels are divided by 2 i.e. 3.8 i.e. n logn
"""

# merge sort space complexity
"""
Oo(n)
because max we'll split main array into 2 sub array copies i.e. O(n)
"""

# merge sort comparison
"""
better than bubble, selection and insertion
because of time complexity
"""

# merge sort logic
"""
# keep breaking arrays into multiple parts until 1
# then merge them back in sorted order via 2 indexes
"""

# program - recursion - merge sort - via copying arrays - https://www.codingninjas.com/codestudio/problems/merge-sort_920442
# logic - break array into two parts and merge them - rest will happen recursively
"""
def merge(arr, start, end):
    mid = start + ((end-start)//2)
    a = arr[start:mid+1]
    b = arr[mid+1:end+1]
    i = 0
    j = 0
    k = start
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
def merge_sort(arr, start, end):
    if start == end:
        return
    mid = start + ((end-start)//2)
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, end)
arr = [5,4,3,1,2,0,10]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
"""

# hw: read: https://www.geeksforgeeks.org/merge-sort/ - esp. first point - esp. drawbacks
"""
merge sort is divide and conquer
merge sort calls itself on 2 divided portions then merges them
stable algo

applications:
sort linkedlist without extra space as in linked lists we can insert in O(1)
coz data is accessed sequentially and random access is low as in linked lists we have to traverse to reach a position

drawbacks:
slower for smaller tasks
requires extra space for temporary array
not adaptable i.e. goes through entire process even if it is sorted
"""

# inversion count logic
"""
how far or close the array is from getting sorted
for sorted array inversion count is 0
for reverse inversion count is maximum

two elements form inversion if they are one after another but first is greater than second
eg: 8421
ans: 6
84 82 81 42 41 21

brute force - count all smaller elements on right side of each element

with merge sort:
divide in 2 parts count inversion while merging, count inversions for merge i.e. mid - point where first array element is greater than 2nd as they are sorted
eg: 0367 1258 --> 01 --> 345 > 2 so 3 inversions total mid - 1 inversions i.e. 4 -1 i.e. 3 inversions
"""

# hw: program: inversion count : https://www.geeksforgeeks.org/merge-sort/ - https://www.geeksforgeeks.org/counting-inversions/
"""
def merge(arr, start, end):
    inversion_count = 0
    mid = start + ((end - start) // 2)
    a = arr[start:mid+1]
    b = arr[mid+1:end+1]
    i = 0
    j = 0
    k = 0
    ans = [0]*(end-start+1)
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ans[k] = a[i]
            i += 1
            k += 1
        else:
            inversion_count += (mid-i+1)
            ans[k] = b[j]
            j += 1
            k += 1
    while i < len(a):
        ans[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        ans[k] = b[j]
        j += 1
        k += 1
    return inversion_count
def merge_sort(arr, start, end):
    inversion_count = 0
    if start >= end:
        return 0
    else:
        mid = start + ((end-start)//2)
        inversion_count += merge_sort(arr, start, mid)
        inversion_count += merge_sort(arr, mid+1, end)
        inversion_count += merge(arr, start, end)
    return inversion_count
print(merge_sort([0,1,3,6,1,2,4,5], 0, 7))
"""

# hw: program: merge sort - in place
# logic - kind of selection sort but we already know min is either on our pointer on left or right array so just compare those
# logic - to check if they are already sorted, compare last element of a with first of b
"""
def merge(arr, start, end):
    mid = start + ((end-start)//2)
    i = start
    j = mid+1
    if arr[mid] <= arr[j]:
        return
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            i += 1
        else:
            temp = arr[j]
            for k in range(j-1, i-1, -1):
                arr[k+1] = arr[k]
            arr[i] = temp
            i += 1
            j += 1
            mid += 1
def merge_sort(arr, start, end):
    if start == end:
        return
    mid = start + ((end-start)//2)
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, end)
arr = [5,4,3,1,2,0,10]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
"""
