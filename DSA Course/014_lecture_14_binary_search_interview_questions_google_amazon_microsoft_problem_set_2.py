# program: find pivot in rotated sorted array
# sorted array -> [1,2,3,7,9]
# sorted rotated array -> [7,9,1,2,3]
# find pivot i.e. 9 or 1 we are solving for 1
# logic: draw graph
# logic: we have start and end value, find mid, if mid value >= start value, we are on first line, move start to mid + 1
# if mid value < start, we are either on peak or further, move end to mid, final element left is min pivot, stop when s crosses e
"""
def get_pivot_rotated_sorted(a):
    start = 0
    end = len(a) - 1
    while start < end:
        mid = start + ((end-start)//2)
        if a[mid] >= a[0]:  # first line
            start = mid + 1
        else:
            end = mid
    return start
print(get_pivot_rotated_sorted([7,9,1,2,3]))
"""

# program: https://www.codingninjas.com/codestudio/problems/search-in-rotated-sorted-array_1082554
# logic: find pivot and see whether value lies between pivot and end or not
# if yes, search on second line i.e. pivot to end, else search on first line i.e. start to pivot - 1
# this way we are deciding which line to apply binary search on, as both a re monotonic functions
def get_pivot_rotated_sorted(a):
    start = 0
    end = len(a) - 1
    while start < end:
        mid = start + ((end-start)//2)
        if a[mid] >= a[0]:  # first line
            start = mid + 1
        else:
            end = mid
    return start
def binary_search(a, n, start, end):
    while start <= end:
        mid = start + ((end-start)//2)
        if n < a[mid]:
            end = mid - 1
        elif n == a[mid]:
            return mid
        elif n > a[mid]:
            start = mid + 1
    return -1
def search_in_rotated_sorted_array(a, n):
    pivot = get_pivot_rotated_sorted(a)
    start = 0
    end = len(a) - 1
    if a[pivot] <= n <= a[end]:
        return binary_search(a, n, pivot, end)
    else:
        return binary_search(a, n, start, pivot - 1)
a = [7,9,1,2,3]
n = 2
print(search_in_rotated_sorted_array(a, n))

# hw: program: alternate approach for https://www.codingninjas.com/codestudio/problems/search-in-rotated-sorted-array_1082554 other than pivot and binary search ine one part
# logic: take start, end, mid
# if midval is same as target, return mid
# elif startval < midval means left part is sorted, check if element lies in range, if so, move end to mid - 1, else move start to mid + 1
# elif start > mid val means left part is not sorted that means right part is sorted, check if element exists in range, if yes, move start to mid + 1, else move end to mid - 1
# use <= and >= where appropriate as we could be on one element only, which itself could be start, end, mid and target
"""
def search_in_rotated_sorted_array(a, target):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high-low)//2)
        # if middle element is target
        if a[mid] == target:
            return mid
        # if left side is sorted
        elif a[low] <= a[mid]:
            # if element is in left side range
            if a[low] <= target <= a[mid]:
                # skip right part
                high = mid - 1
            else:
                # skip left part
                low = mid + 1
        # left part is not sorted i.e. right part is sorted
        else:
            # element lies in right part
            if a[mid+1] <= target <= a[high]:
                # skip left part
                low = mid + 1
            # element lies in left part
            else:
                # skip right part
                high = mid - 1
    return -1
a = [7,9,1,2,3]
n = 2
print(search_in_rotated_sorted_array(a, n))
"""

# program: https://www.codingninjas.com/codestudio/problems/square-root_893351
# logic for int: binary search from 0 to that number and square and see, if > move end back, if < save as possible ans for not exact square and move start forward, stop when start and end cross, take care of intoverflow in other language by using long long int
# logic for precision: keep factor as one and for needed precision divide it by 10 each time, and then keep adding factor to 0 and check for smaller or equal ans
"""
def int_sqrt(n):
    start = 0
    end = n
    ans = -1
    while start <= end:
        mid = start + ((end-start)//2)
        sq = mid*mid
        if sq == n:
            return mid
        elif sq > n:
            end = end - 1
        elif sq < n:
            ans = mid
            start = mid + 1
    return ans
def decimal_sqrt(n, precision):
    factor = 1
    ans = int_sqrt(n)
    for i in range(precision):
        factor = factor/10
        python_precision = f".{i+1}f"
        j = ans
        while j*j < n:
            ans = j
            j += factor
            j = float(f"{j:{python_precision}}")
    return ans
print(decimal_sqrt(37, 3))
"""
