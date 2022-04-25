# https://www.codingninjas.com/codestudio/problem-details/first-and-last-position-of-an-element-in-sorted-array_1082549
# not found - -1
# found multiple - start and end
# found one - start and end is same
# find a mid that matches key
# then go backward for first occurence and forward for right occurence
# and rest of the looping remains same i.e. go forward is key is greater than mid element else backward
# ------------------------------------------------------------------------------------------------------
# find total number of occurences of a number in an array
# first use above program for finding start and end
# then do end - start + 1 if they are not -1
"""
def first_occurence(a, key):
    start = 0
    end = len(a) - 1
    mid = start + (end - start) // 2
    ans = -1
    while start <= end:
        if a[mid] == key:
            ans = mid
            end = mid - 1
        elif key > a[mid]:
            start = mid + 1
        elif key < a[mid]:
            end = mid - 1
        mid = start + (end - start) // 2
    return ans
def last_occurence(a, key):
    start = 0
    end = len(a) - 1
    mid = start + (end - start) // 2
    ans = -1
    while start <= end:
        if a[mid] == key:
            ans = mid
            start = mid + 1
        elif key > a[mid]:
            start = mid + 1
        elif key < a[mid]:
            end = mid - 1
        mid = start + (end - start) // 2
    return ans
def firstAndLastPosition(arr, n, k):
    start = first_occurence(arr, k)
    end = last_occurence(arr,k)
    return (start, end)
def find_total_no_of_occurences(arr, n, k):
    res = firstAndLastPosition(arr, n, k)
    if res != (-1,-1):
        return res[1] - res[0] + 1
    else:
        return 0
print(find_total_no_of_occurences([1,2,3,3,3,5], 6, 3))
"""

# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# eg:
#     2
#  /    1
# 0       0
# find mid
# if mid < mid + 1
# that means peak is either at mid + 1 or ahead
# hence make start as mid + 1
# else if mid > mid + 1
# that means peak can either be mid or backwards
# hence make end as mid
# continue
"""
class Solution:
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr)
        mid = start + (end - start) // 2
        while start < end:
            if arr[mid] <= arr[mid+1]:
                start = mid + 1
            else:
                end = mid
            mid = start + (end - start) // 2
        return mid
"""

# homework - optimization pending
# https://leetcode.com/problems/find-pivot-index/
"""
class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            right_sum = total_sum - left_sum - x
            if left_sum == right_sum:
                return i
            left_sum += x
        return -1
"""