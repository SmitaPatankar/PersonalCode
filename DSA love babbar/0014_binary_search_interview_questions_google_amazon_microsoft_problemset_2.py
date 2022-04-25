# find pivot in rotated sorted array
# eg: 12345
# rotated to 45123
# one line is 45 going up
# other line is 123 going up
# in between the lowest point is at the start of second line i.e. 1
# we have to find this
# find mid
# if mid >= start that means we are on first line
# hence make start = mid + 1
# else second line including pivot
# hence make end = mid
# continue
# stop when start=end and return value
"""
def get_pivot(arr):
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2
    while start < end:
        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid
        mid = start + (end - start) // 2
    return start  # or end
arr = [8, 10, 17, 1, 3, 4]
print(get_pivot(arr))
"""

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# show present or absent
# APPROACH 1-------------->
# find pivot as per above program
# compare key with pivot
# if key lies between pivot and end included, search in 2nd line i.e. start=pivot
# else search in first line i.e. end = pivot - 1
# O(logn)
# APPROACH 2-----------> homework - main solution pending - optimization pending
# find mid
# check which part is sorted
# on that part, based on target move start and/or end
# O(log n)
# APPROACH 3---------> homework - main solution pending - optimization pending
# similar as first - but write 50% of code
# O(log n)
"""
def get_pivot(arr):  # copied
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2
    while start < end:
        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid
        mid = start + (end - start) // 2
    return start
def binary_search(a, key, start, end):
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
def search(arr, key):
    pivot = get_pivot(arr)
    if key >= arr[pivot] and key <= arr[len(arr) - 1]:
        return binary_search(arr, key, pivot, len(arr) - 1)
    else:
        return binary_search(arr, key, 0, pivot - 1)
print(search([4,5,1,2,3], 5))
"""


# https://www.codingninjas.com/codestudio/problems/square-root_893351
# square root using binary search
# brute force - rootn complexity
# binary search - logn complexity
# search space - where our ans could like
# i.e. 0 to the number
# monotonous flow - binary search
# if square of mid is greater than number, move end backwards
# else if smaller then move start forward
# else if same, return value
"""
def sqrtN(n):
    start = 0
    end = n
    mid = start + (end - start) // 2
    ans = -1
    while start <= end:
        sq = mid*mid  # use long long int for this
        if sq == n:
            return mid
        elif sq < n:
            ans = mid
            start = mid + 1
        elif sq > n:
            end = mid - 1
        mid = start + (end - start)//2
    return ans
print(sqrtN(9999))
"""

# continue above square root program with decimals of square root
# brute force - keep adding .1 and check and stop when greater
# similarly for further points 0.01 and so on
# save it in double
# pending - fix this as per python floating point behaviour
"""
def sqrtN(n):
    start = 0
    end = n
    mid = start + (end - start) // 2
    ans = -1
    while start <= end:
        sq = mid*mid  # use long long int for this
        if sq == n:
            return mid
        elif sq < n:
            ans = mid
            start = mid + 1
        elif sq > n:
            end = mid - 1
        mid = start + (end - start)//2
    return ans
def more_precision(n, precision, temp_sol):
    factor = 1
    ans = temp_sol
    for i in range(0, precision):
        factor = factor / 10
        j = ans
        while j*j < n:
            ans = j
            j = j + factor
    return ans
n = 101
temp_sol = sqrtN(n)
print(more_precision(n, 3, temp_sol))
"""