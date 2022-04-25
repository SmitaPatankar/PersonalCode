# array swap alternate program
# 1 2 3 4 5 6 --> 2 1 4 3 6 5
# 1 2 3 4 5 6 7 --> 2 1 4 3 6 5 7
"""
def swap_alternate(a, size):
    for i in range(0, size, 2):
        if i+1 < size:
            a[i], a[i+1] = a[i+1], a[i]
def print_array(a, size):
    for i in range(0, size, 1):
        print(a[i], end=" ")
    print()
def main():
    a = [1, 2, 3, 4, 5, 6, 7]
    size = 7
    print(a)
    swap_alternate(a, size)
    print(a)
    b = [1, 2, 3, 4, 5, 6, 7]
    size = 7
    print(b)
    swap_alternate(b, size)
    print(b)
main()
"""

# swap 2 numbers without function - with extra var
"""
a = 1
b = 2
temp = a
a = b
b = temp
print(a)
print(b)
"""

# swap 2 numbers without function - without extra var
"""
a = 1
b = 2
a = a + b
b = a - b
print(a)
print(b)
"""

# https://www.codingninjas.com/codestudio/problems/unique_625159
# array of size n
# n = 2m + 1
# m numbers are present twice
# 1 number is present only once
# find the unique number
# brute force - save count of each and return where count is 1
# better approach - xor everything together - xor with same element returns 0 and xor of 0 and other element returns other element
# eg: 2 ^ 1 ^ 5 ^ 1 ^ = 0 ^ 5 = 5
"""
def findUnique(arr, n):
    ans = 0
    for i in range(len(arr)):
        ans = ans ^ arr[i]
    return ans
"""

# https://leetcode.com/problems/unique-number-of-occurrences/
# homework - optimization pending
# check if counts of all elements are unique or not in an array
"""
class Solution:
    def uniqueOccurrences(self, arr):
        count_dict = dict()
        for element in arr:
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1
        visited = set()
        for element, count in count_dict.items():
            if count in visited:
                return False
            visited.add(count)
        return True
"""

# https://www.codingninjas.com/codestudio/problem-details/duplicate-in-array_893397
# duplicates in array
# array of size n
# 1 to n-1 are present
# one of them is present twice
# find that number
# brute force - count and return with duplicate count
# other approach - xor 1 to n with given elements --> 1 to n will cancel out
"""
def findDuplicate(arr):
    ans = 0
    for i in range(1, len(arr)):
        ans = ans ^ i
    for i in range(len(arr)):
        ans = ans ^ arr[i]
    return ans
"""

# homework - optimization pending
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# array of length n
# all elements are in range of 1 to n
# each integer appears once or twice
# find all those that appear twice
"""
class Solution:
    def findDuplicates(self, nums):
        res = []
        for element in nums:
            if nums[abs(element)-1] < 0:
                res.append(abs(element))
            else:
                nums[abs(element) - 1] = nums[abs(element) - 1] * -1
        return res
"""

# https://www.codingninjas.com/codestudio/problem-details/intersection-of-2-arrays_1082149
# array a - size n
# array b - size m
# sorted in non decreasing order
# eg: a = [1,2,2,2,3,4]
# eg: b = [2,2,3,3]
# eg: o/p = [2,3,3]
# find intersection i.e. common elements
# solve in O(max(n,m)) time complexity
# brute force - check each element in first array with each element in second array
# optimization with it - break when other array element is greater
# optimization in another program - two pointer approach
# start both at 0 index
# if first is less than 2nd, move first forward
# if first is eq to second, move both forward
# if first is greater than 2nd, move 2nd forward
"""
def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    result = []
    for i in range(n):
        element = arr[i]
        for j in range(m):
            if element < brr[j]:
                break
            if element == brr[j]:
                result.append(element)
                brr[j] = -1
                break
    return result

def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    result = []
    i = 0
    j = 0
    while i < n and j < m:
        if arr[i] < brr[j]:
            i += 1
        elif arr[i] == brr[j]:
            result.append(arr[i])
            i += 1
            j += 1
        elif arr[i] > brr[j]:
            j += 1
    return result
"""

# https://www.codingninjas.com/codestudio/problem-details/pair-sum_697295
"""
def pairSum(arr, s):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == s:
                temp = [arr[i],arr[j]]
                result.append([min(temp), max(temp)])
    return sorted(result)
"""

# homework - main solution pending - optimization pending
# https://www.codingninjas.com/codestudio/problems/triplets-with-given-sum_893028
# sort 0s and 1s program
# approach 1 - count and then put that many from start - traverse 2 times
# approach 2 - sort - n log n
# approach 3 - 2 pointer - 2n
# if left is 0 move forward
# if right is 1 move back
# if both are wrong, swap
# when i >= j, stop

# homework - main solution pending - optimization pending
# https://www.codingninjas.com/codestudio/problems/sort-0-1-2_631055
