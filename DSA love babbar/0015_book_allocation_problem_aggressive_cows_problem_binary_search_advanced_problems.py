# when to use binary search
"""
when search space can be reduced based on condition
i.e. keep one part and discard another
"""

# https://www.codingninjas.com/codestudio/problem-details/allocate-books_1090540
# book allocation problem
# array
# ith element shows pages in ith book
# m students
# each student should get one book
# each book should be allocated
# book allocation should be continuous
# do this such that maximum pages to a student is minimum
# n is size of array
# return max pages allocated to student which are minimum
# eg: 10 20 30 40
# 10 | 20 30 40 -> max is 90
# 10 20 | 30 40 -> max is 70
# 10 20 30 | 40 -> max is 60
# min is 60
# return -1 if not found
# ans search space will start from min and end at sum of all
# lets start from 0 to sum
# eg: 0 to 100
# mid is 50
# check if 50 is possible ans
# barrier at 10 + 20 because it is <= 50
# another barrier at 30 because it is <= 50 - but we have only 2 students
# 50 is not possible solution
# sums towards the left will be < 50 that will also need more than 2 students
# hence move to right
# pending - try thinking on our own
# 75 - possible solution - 10 20 30 | 40 - save 75 as ans
# now all further numbers are possible
# but we need minimum
# so make end as end - 1
# 62 is possible
# 56 not possible
# 59 not possible
# 60 possible
# s > e stop
"""
def is_possible(arr, n, m, mid):
    student_count = 1
    page_sum = 0
    for i in range(0, n):
        if page_sum + arr[i] <= mid:
            page_sum += arr[i]
        else:
            student_count += 1
            if student_count > m or arr[i] > mid:
                return False
            else:
                page_sum = arr[i]
    return True
def allocate_books(arr, n, m):
    start = 0
    end = sum(arr)
    mid = start + (end-start)//2
    ans = -1
    while start <= end:
        if is_possible(arr, n, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
        mid = start + (end - start)//2
    return ans
print(allocate_books([10,20,30,40], 4, 3))
"""

# homework - optimization pending by comparing with Love
# https://www.codingninjas.com/codestudio/problems/painter's-partition-problem_1089557?source=youtube&campaign=love_babbar_codestudio2&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio2
# painters partition problem
# array of length n
# k no of painters
# painting of 1 unit board takes 1 unit time
# painter can paint continuous sections of boards
# minimum time to paint complete array
# 5 5 5 5
# 5 5 | 5 5
# minimum time 10 units
"""
def is_possible(arr, m, mid):
    painter_count = 1
    board_length_sum = 0
    for i in range(0, len(arr)):
        if board_length_sum + arr[i] <= mid:
            board_length_sum += arr[i]
        else:
            painter_count += 1
            if painter_count > m or arr[i] > mid:
                return False
            else:
                board_length_sum = arr[i]
    return True
def allocate_boards(arr, m):
    start = 0
    end = sum(arr)
    mid = start + (end - start) // 2
    ans = -1
    while start <= end:
        if is_possible(arr, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
        mid = start + (end - start) // 2
    return ans
def findLargestMinDistance(boards:list, k:int):
    return allocate_boards(boards, k)
"""

# https://www.codingninjas.com/codestudio/problems/aggressive-cows_1082559?source=youtube&campaign=love_babbar_codestudio2&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio2
# aggressive cows problem
# array of length n
# consists of position of stall
# n stalls
# k aggressive cows
# allocate stalls to cows such that minimum distance is max between each one of them
# return largest minimum distance
# k = 2
# 4 2 1 3 6
# 4 - 6 = 2
# 4 - 3 = 1
# 4 - 1 = 3
# 4 - 2 = 2
# 2 - 6 = 4
# 2 - 3 = 1
# 2 - 1 = 1
# 1 - 6 = 5 *****
# 1 - 3 = 2
# 3 - 6 = 3
# ------------------
# start with 0 distance
# end = max of array - min of array i.e. 6-1 = 5
# 1 2 3 4 6 - array
# 0 1 2 3 4 5 - possible answers i.e search space
# mid = 2
# 1 and 2 is not possible
# 1 and 3 is possible
# 2 is possible ans
# move forward with distance search space i.e. 3 to 5
# mid is 4
# 4 is possible between (5 is possible between 1 and 6)
# mid is 5
# return
# pending - think on our own
"""
def is_possible(stalls, k, mid):
    cow_count = 1
    last_pos = stalls[0]
    for i in range(0, len(stalls)):
        if abs(stalls[i] - last_pos) >= mid:
            cow_count += 1
            if cow_count == k:
                return True
            else:
                last_pos = stalls[i]
    return False
def aggressive_cows(stalls, k):
    stalls.sort()
    s = 0
    maxi = max(stalls)
    e = maxi
    mid = s + (e - s)//2
    ans = -1
    while s <= e:
        if is_possible(stalls, k, mid):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
        mid = s + (e - s)//2
    return ans
print(aggressive_cows([4, 2, 1, 3, 6], 2))
"""

# homework - main solution pending - optimization pending
# https://www.spoj.com/problems/EKO/
# EKO - SPOJ

# homework - main solution pending - optimization pending
# https://www.spoj.com/problems/PRATA/
# PRATA SPOJ

# homework - main solution pending - optimization pending
# https://www.hackerrank.com/challenges/beautiful-triplets/problem
# beautiful triplets
