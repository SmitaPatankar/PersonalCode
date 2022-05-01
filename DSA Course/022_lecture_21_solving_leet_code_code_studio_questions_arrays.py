# program: https://leetcode.com/problems/rotate-array/
# rotate array elements by given count
# eg: {1,7,9,11} i.e. {9,11,1,7} for 2
# eg: {0,1,2,3,4,5,6,7,8,9} i.e. {9,8,7,0,1,2,3,4,5,6} for 3
# logic: use extra array
# logic: mod calculated position with length of array to directly jump to accurate position by skipping unnecessary calculations
# eg: [0,1,2,3,4]  # 3
# [2,3,4,0,1]  # pos = i + n i.e. 4 + 3 i.e. 7 - map 7 to 2 i.e. 7%5 = 2
# logic % n always gives ans in 0 to n-1
# logic - shifting ith term by k positions in cyclic way
# cyclic means going backwards if no place forwards
# copy coz question says modify nums in place
# hw: time complexity: O(n)
# hw: space complexity: O(n)
"""
def rotate_array(a, n):
    ans = [None]*len(a)
    for i in range(len(a)):
        ans[(i+n) % len(a)] = a[i]
    a[:] = ans[:]
arr = [1,7,9,11]
print(arr)
n = 2
print(n)
rotate_array(arr,n)
print(arr)
"""

# program: https://leetcode.com/problems/rotate-array/
# real in place approach
# logic:
# n = n % len(a) to skip unnecessary rotation to be back at original place
# q:   0 1 2 3 4 5 6 by 3
#      6 5 4 3 2 1 0 --> reverse
#      4 5 6 3 2 1 0 --> reverse first 3 elements
#      4 5 6 0 1 2 3 --> reverse remaining elements
# ans: 4 5 6 0 1 2 3
"""
def rotate_array(arr, n):
    n = n % len(arr)
    reverse(arr, 0, len(arr)-1)
    reverse(arr, 0, n-1)
    reverse(arr, n, len(arr)-1)
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
a = [0,1,2,3,4,5,6]
n = 3
print(a)
print(n)
rotate_array(a, n)
print(a)
"""

# program: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# logic:
# sorted rotated:
# [3,4,5,1,2]
# [2,3,4,5,1,2]
# [3,4,5,1,2,2]
# [2,2,2,1,2,2,2]
# greater than previous all, one is smaller than previous, and last is smaller than first
# only sorted:
# [1,2,3,4,5,6]
# greater than previous all
# not sorted itself:
# [3,5,7,1,6]
# greater, greater, smaller, greater pairs mix
# only one dip should exist, and last element shud be < than first (cyclic)
# [2,2,2,2,2,2] --> false
# hw: time complexity: O(n)
# hw: space complexity: O(1)
"""
def check_sorted_rotated(arr):
    print(arr)
    n = len(arr)
    dip = 0
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            dip += 1
    if dip and arr[n-1] <= arr[0]:
        return True
    return False
arr = [3,4,5,1,2]
print(check_sorted_rotated(arr))
arr = [1,2,3,4,5,6]
print(check_sorted_rotated(arr))
arr = [3,5,7,1,6]
print(check_sorted_rotated(arr))
arr = [1,1,1,1]
print(check_sorted_rotated(arr))
"""

# program: https://www.codingninjas.com/codestudio/problems/sum-of-two-arrays_893186
# eg: 1234 + 6 = 1240
# ans
# store_ans = ans % 10
# carry = ans / 10
# eg: 9+9 18 --> 18 % 10 = 8, 18/10 = 1
# start addition from last element using i,j
# handle first array big, 2nd array big, both array big with carry
# logic, find cases first
# hw: time complexity: O(n+m)
# hw: space complexity: O(n+m)
"""
def sum_arrays(a, b):
    ans = []
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    while i >= 0 and j >= 0:
        total = a[i] + b[j] + carry
        ans.append(total % 10)
        carry = total // 10
        i -= 1
        j -= 1
    while i >= 0:
        total = a[i] + carry
        ans.append(total%10)
        carry = total / 10
        i -= 1
    while j > 0:
        total = b[j] + carry
        ans.append(total%10)
        carry = total / 10
        j -= 1
    if carry:
        ans.append(carry)
    reverse(ans)
    return ans
def reverse(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
a = [9,9,9]
b = [1,2,3]
print(a)
print(b)
print(sum_arrays(a,b))
"""
