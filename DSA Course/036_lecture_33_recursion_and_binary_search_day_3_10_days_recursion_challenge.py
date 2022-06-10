# program - recursion - issorted
"""
def is_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] < arr[1]:
        return is_sorted(arr[1:])
    else:
        return False
print(is_sorted([1,2,3,4,5]))
print(is_sorted([]))
print(is_sorted([1]))
print(is_sorted([2,1,5,8,-1]))
"""

# program - recursion - sum of array
"""
def sum_of_array(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum(arr[1:])
print(sum_of_array([1,2,3,4,5]))
print(sum_of_array([]))
print(sum_of_array([1]))
"""

# program - recursion - linear search
"""
def linear_search(arr, n):
    if not arr:
        return False
    if arr[0] == n:
        return True
    else:
        return linear_search(arr[1:], n)
print(linear_search([1,2,3,4,5], 3))
print(linear_search([1,2,3,4,5], 6))
print(linear_search([1,2,3,4,5], 0))
"""

# program - recursion - binary search - https://www.codingninjas.com/codestudio/problems/binary-search_972
"""
def binary_search(arr, n, start, end):
    if start > end:
        return -1
    mid = start + ((end-start)//2)
    if arr[mid] == n:
        return mid
    if n < arr[mid]:
        return binary_search(arr, n, start=start, end=mid-1)
    else:
        return binary_search(arr, n, start=mid+1, end=end)
print(binary_search([1,2,3,4,5],3, 0, 4))
print(binary_search([1,2,3,4,5],30, 0, 4))
print(binary_search([1,2,3,4,5],-1, 0, 4))
"""

# todo: hw: program: recursion: binary: all questions from lecture 12 to 15 without loops if missed below

# todo: compare with actual solution
# hw: program: recursion: binary: first and last position
"""
def first_position(arr, n, start, end, ans=-1):
    if start > end:
        return ans
    else:
        mid = start + ((end-start)//2)
        if arr[mid] == n:
            return first_position(arr, n, start=start, end=mid-1, ans=mid)
        elif n < arr[mid]:
            return first_position(arr, n, start=start, end=mid-1, ans=ans)
        else:
            return first_position(arr, n, start=mid+1, end=end, ans=ans)
def last_position(arr, n, start, end, ans=-1):
    if start > end:
        return ans
    else:
        mid = start + ((end-start)//2)
        if arr[mid] == n:
            return first_position(arr, n, start=mid+1, end=end, ans=mid)
        elif n > arr[mid]:
            return first_position(arr, n, start=mid+1, end=end, ans=ans)
        else:
            return first_position(arr, n, start=start, end=mid-1, ans=ans)
def first_and_last_position(arr, n):
    return [first_position(arr, n, 0, len(arr)-1), last_position(arr, n, 0, len(arr)-1)]
arr = [1,2,2,2,3,4,5]
n = 2
print(f"in array {arr} - start and end positions of {n} are {first_and_last_position(arr, n)}")
"""

# todo: compare with actual solution
# hw: program: recursion: binary: peak in mountain
"""
def mountain_peak_index(arr, ans, start, end):
    if start >= end:
        return ans
    else:
        mid = start + ((end-start)//2)
        if arr[mid] < arr[mid+1]:
            return mountain_peak_index(arr, ans, mid + 1, end)
        else:
            ans = mid
            return mountain_peak_index(arr, ans, start, mid)
print(mountain_peak_index([1,2,3,5,4,1,-1,0], -1, 0, 7))
"""

# todo: compare with actual solution
# hw: program: recursion: binary: aggressive cows
# array of stall positions
# k cows shudnt fight
# i.e. find max min distance
# unsorted
"""
def is_possible_solution(arr, k, mid):
    current_cow_number = 1
    last_cow_position = 0
    print(f"placing cow number 0 at position {arr[last_cow_position]}")
    for i in range(1, len(arr)):
        if arr[i] - arr[last_cow_position] >= mid:
            print(f"placing cow number {current_cow_number} at position {arr[i]}")
            current_cow_number += 1
            last_cow_position = i
        if current_cow_number == k:
            return True
def max_min_distance(arr, k, start, end, ans):
    if start > end:
        return ans
    mid = start + ((end-start)//2)
    if is_possible_solution(arr, k, mid):
        print(f"{mid} possible solution-----------------")
        return max_min_distance(arr, k, start=mid+1, end=end, ans=mid)
    else:
        print(f"{mid} not a possible solution--------------")
        return max_min_distance(arr, k, start=start, end=mid-1, ans=ans)
def aggressive_cows(arr, k):
    arr.sort()
    start = 0
    end = arr[-1]
    ans = -1
    return max_min_distance(arr, k, start, end, ans)
print(aggressive_cows([4,2,1,3,6], 2))
print(aggressive_cows([4,2,1,3,6], 3))
"""

# todo: compare with actual solution
# hw: program: recursion: binary: book allocation
# array with pages in each book
# m students
# find minimum max pages to student
# all students and books should be used
"""
def is_possible_solution(arr, m, mid):
    current_student_number = 0
    current_student_pages = 0
    for i in range(0, len(arr)):
        if current_student_pages + arr[i] <= mid:
            current_student_pages += arr[i]
        else:
            current_student_number += 1
            if current_student_number == m or arr[i] > mid:
                return False
            else:
                current_student_pages = arr[i]
    return True
def min_max_pages(arr, m, start, end, ans):
    if start > end:
        return ans
    mid = start + ((end-start)//2)
    if is_possible_solution(arr, m, mid):
        print(f"{mid} possible solution-----------------")
        return min_max_pages(arr, m, start=start, end=mid-1, ans=mid)
    else:
        print(f"{mid} not a possible solution--------------")
        return min_max_pages(arr, m, start=mid+1, end=end, ans=ans)
arr = [10,20,30,40]
m = 2
start = 0
end = sum(arr)
ans = -1
print(min_max_pages(arr, m, start, end, ans))
"""

# todo: compare with actual solution
# hw: program: recursion: binary: pivot
"""
def is_pivot_index(arr, i, left_sum,right_sum):
    print(f"current element is {arr[i]} left sum is {left_sum} right sum is {right_sum}")
    if left_sum == right_sum:
        return True
    else:
        return False
def get_pivot_index(arr, i, left_sum,right_sum):
    if is_pivot_index(arr, i, left_sum, right_sum):
        return i
    else:
        left_sum += arr[i]
        i += 1
        right_sum -= arr[i]
        return get_pivot_index(arr, i, left_sum, right_sum)
arr = [1, 7, 3, 6, 5, 6]
i = 0
left_sum = 0
right_sum = sum(arr)-arr[i]
print(get_pivot_index([1, 7, 3, 6, 5, 6], i, left_sum, right_sum))
"""

# todo: compare with actual solution
# hw: program: recursion: binary: search in rotated array
# 		9
# 	7		1
#  				2
# 					3
"""
def pivot(arr, start, end):
    if start >= end:
        return start
    mid = start + ((end-start)//2)
    if arr[mid] >= arr[0]:
        start = mid + 1
    else:
        end = mid
    return pivot(arr, start, end)
def search(arr, n, start, end):
    if start > end:
        return -1
    mid = start + ((end-start)//2)
    if arr[mid] == n:
        return mid
    else:
        if arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
        return search(arr, n, start, end)
def main():
    arr = [7,9,1,2,3]
    start = 0
    end = 4
    n = 9
    p = pivot(arr, start, end)
    if arr[end] >= n >= arr[p]:
        print(search(arr, n, p, end))
    else:
        print(search(arr, n, start, p-1))
main()
"""

# todo: compare with actual solution
# hw: program: recursion: binary: sqrt
"""
def sqrt(n, start, end):
    if start > end:
        return -1
    mid = start + ((end-start)//2)
    sq = mid * mid
    if sq == n:
        return mid
    elif sq > n:
        return sqrt(n, start, mid-1)
    else:
        return sqrt(n, mid+1, end)
def main():
    n = 49
    start = 0
    end = n
    print(sqrt(n, start, end))
main()
"""
