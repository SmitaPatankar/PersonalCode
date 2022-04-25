# binary search
"""
values in increasing/decreasing order i.e. monotonic function
1. find mid element of array
2. check if search element equals mid element
3. if yes, return index
4. if not, check if search element is greater than mid element, then continue the same process on right part else on left part

formula for mid index is (start + end) // 2

if no part present on the chosen side, not found, return -1

do this till start <= end
if start goes forward then end, that's a problem
when end goes backward from start, that's a problem

s+e from (s+e)/2 can result in a really larger number out of int range
hence use s + (e-s)/2

size reduces by 2 each time
100   --> 500   --> 250   --> 125   --> 62    --> 31    --> 15    --> 7     --> 3     --> 1
1/2^0 --> n/2^1 --> n/2^2 --> n/2^3 --> n/2^4 --> n/2^5 --> n/2^6 --> n/2^7 --> n/2^8 --> n/2^9

ends at n/2^k when size is 1
i.e. n/2^k = 1
i.e. n = 2^k
k = log n

2 raised to what is n?
logn
i.e. out complexity

time - O(logn)

10 searches instead of 1000 like linear
"""


# binary search program
def binary_search(a, key):
    start = 0
    end = len(a) - 1
    mid = start + (end-start)//2
    while start <= end:
        if a[mid] == key:
            return mid
        elif key > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = start + (end - start) // 2
    return -1


even = [2, 4, 6, 8, 12, 18]
odd = [3, 8, 11, 14, 16]
print(f"index of 12 in even array is {binary_search(even, 12)}")
print(f"index of 4 in even array is {binary_search(even, 4)}")
print(f"index of 20 in even array is {binary_search(even, 20)}")
print(f"index of 1 in even array is {binary_search(even, 1)}")
print(f"index of 12 in odd array is {binary_search(odd, 14)}")
print(f"index of 4 in odd array is {binary_search(odd, 3)}")
print(f"index of 20 in odd array is {binary_search(odd, 18)}")
print(f"index of 1 in odd array is {binary_search(odd, 2)}")
