# program: https://www.codingninjas.com/codestudio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549
# program: total occurences of number in array
# logic: for first occurence below
# start, end, mid
# compare with mid, if found, store it and move end backwards
# else if smaller, move end backward
# else if larger, move start forward
# logic: similarly for last occurence where you move mid forwards when found
# logic: same for total no. of occurences program i.e. last occurence - first occurence + 1
"""
def first_occurence(a, n):
    start = 0
    end = len(a) - 1
    ans = -1
    while start <= end:
        mid = start + ((end - start) // 2)
        if n == a[mid]:
            ans = mid
            end = mid - 1
        elif n < a[mid]:
            end = mid - 1
        elif n > mid:
            start = mid + 1
    return ans
def last_occurence(a, n):
    start = 0
    end = len(a) - 1
    ans = -1
    while start <= end:
        mid = start + ((end-start)//2)
        if n == a[mid]:
            ans = mid
            start = mid + 1
        elif n < a[mid]:
            end = mid - 1
        elif n > a[mid]:
            start = mid + 1
    return ans
def first_and_last_occurence(a, n):
    return (first_occurence(a, n), last_occurence(a, n))
a = [1,2,3,3,4,5]
b = [1,2,5,5,5,5,8,10,12]
print(first_and_last_occurence(a, 3))
print(first_and_last_occurence(b, 5))
"""

# todo: program: revise
# program: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# length >= 3
# always mountain
# between first and element there is an index i
# elements to the left of ith index are smaller than ith element and right ones are larger
# eg: 010  --> 1
# eg: 0210 --> 2
# eg: 0 10  5   2 --> 10
# eg: 3 4   5   1 --> 5
# lefter elements are a[i] < a[i+1]
# center element is  a[i-1] < a[i] > a[i+1]
# righter elements are a[i] > a[i+1]
# dry run
# 0 1   2  3    4   5   6   7   8   9   10  11
# 5 6   7   8   9   10  9   8   7   6   5   4
# start     =   0   0   3   5
# end       =   11  5   5   5
# mid       =   5   2   4   stop
# midval    =   10  7   9   stop
# logic: if mid value < next value, mid is below peak, move start to mid + 1, if mid value > next value, we are either on mid after that, move end to mid, final element left is peak
"""
def find_peak_element(a):
    start = 0
    end = len(a) - 1
    while start < end:  # didnt do <= bcoz we dont want only one element where we compare it to next coz we have already done that
        mid = start + ((end-start)//2)
        if a[mid] < a[mid+1]:  # left side
            start = mid + 1
        else:  # peak or right side
            end = mid  # not doing mid - 1 coz peak could be mid itself
    return a[start]
a = [3,4,5,1]
print(find_peak_element(a))
"""

# hw: program: https://leetcode.com/problems/find-pivot-index/
# sum of all numbers to left of index is equal to sum of all numbers to right
# return leftmost pivot index, if not return -1
#      0 1 2 3 4 5
# eg: [1,7,3,6,5,6] --> index 3
# logic: initially left sum is 0 and right sum is total, at start of iteration right sum = right - current, if both are same, retrun, at end of iteration left sum = left + current
"""
def find_pivot(a):
    left_sum = 0
    right_sum = sum(a)
    for i in range(len(a)):
        right_sum -= a[i]
        if left_sum == right_sum:
            return i
        left_sum += a[i]
    return -1
a = [1,7,3,6,5,6]
print(find_pivot(a))
"""
