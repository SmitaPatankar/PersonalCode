# program: https://www.codingninjas.com/codestudio/problems/ayush-and-ninja-test_1097574
# program: book allocation problem
# array arr of integers
# arr[i] shows no. of pages in ith book
# n books
# m no. of students
# allocate books to students:
# each student has atleast one book
# each book should be alloted to a student
# book allocation in contiguous manner
# max number of pages assigned to a student is minimum
# constraints:
# n and m is between 2 and 10^3
# arr[i] is between 1 and 10^9
# eg:
# n = no. of books = 4
# m = no. of students = 2
#        0  1   2  3
# arr = [10,20,30,40]
# ans is 10 20 30, 40
# logic:
# max no. of pages that can be alloted to a person will lie between 0(hypothetical) and sum of all pages count(hypothetical)
# start, end, mid - check if mid is possible solution by making partitions with sum <= midval, if students fit in or are less, possible solution, look for smaller solution by doing end = mid - 1
# else: check greater solution as start = mid + 1
# for possible solution, keep track of student and increment when sum exceeds, stop when student count increases || individual value is > max_sum coz we shudnt allot > value at all
"""
def sum_total(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total
def partition(arr, m):
    start = 0
    end = sum_total(arr)
    ans = -1
    while start <= end:
        mid = start + ((end-start)//2)
        if check_possible(arr, mid, m):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
def check_possible(arr, max_sum, no_of_students):
    student_number = 1
    page_sum = 0
    for i in range(0, len(arr)):
        if page_sum + arr[i] <= max_sum:
            page_sum += arr[i]
        else:
            student_number += 1
            if student_number > no_of_students or arr[i] > max_sum:
                return False
            else:
                page_sum = arr[i]
    return True
print(partition([10,20,30,40], 2))
"""

# hw: program: https://www.codingninjas.com/codestudio/problems/painter's-partition-problem_1089557
# arr of length n
# k no. of painters
# 1 unit board takes 1 unit time
# painter can paint continuous sections
# minimum time to paint array
# eg:
#        0 1 2 3
# arr = [5,5,5,5]
# n = length = 4
# k = no. of painters = 2
# partition boards for painters to get min. time by one who has to paint max
# logic: same as above
"""
def find_max_boards_for_one_painter(arr, k):
    start = 0
    end = sum(arr)
    ans = -1
    while start <= end:
        mid = start + ((end-start)//2)
        if is_possible(arr, k, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
def is_possible(arr, no_of_painters, max_sum):
    painter_number = 1
    board_sum = 0
    for i in range(len(arr)):
        if board_sum + arr[i] <= max_sum:
            board_sum += arr[i]
        else:
            painter_number += 1
            if painter_number > no_of_painters or arr[i] > max_sum:
                return False
            else:
                board_sum = arr[i]
    return True
print(find_max_boards_for_one_painter([5,5,5,5],2))
"""

# todo: program: revise
# program: https://www.codingninjas.com/codestudio/problems/aggressive-cows_1082559
# array arr for positions of stalls
# length n
# k number of aggressive cows
# assign cows to stalls such that they don't fight
# i.e. minimum distance between any of them is as large as possible
# i.e return largest minimum distance
#      0 1 2 3 4
# eg: [4 2 1 3 6]
# k = 2
# 1 and 6 i.e. 5
# when to use binary search:
# use binary search when possible solution helps eliminate search space
# here if greater number makes cows fight, smaller will also do the same so neglect smaller and should be monotonic
# logic:
# min = 0(hypothetical), max=largest slot, mid
# stop placing 2 cows when distance >= mid, s = mid + 1
# if you have more cows left, e = mid - 1
"""
def maximum(arr):
    m = -1
    for i in range(0, len(arr)):
        if arr[i] > m:
            m = arr[i]
    return m
def find_largest_minimum_distance(arr, k):
    arr.sort()
    start = 0
    end = maximum(arr)
    ans = -1
    while start <= end:
        mid = start + ((end-start)//2)
        if is_possible_solution(arr, mid, k):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans
def is_possible_solution(arr, min_distance, no_of_cows):
    cow_number = 1
    last_position = 0
    for i in range(0, len(arr)):
        if arr[i] - arr[last_position] >= min_distance:
            cow_number += 1
            if cow_number == no_of_cows:
                return True
            else:
                last_position = i
    return False
print(find_largest_minimum_distance([4,2,1,3,6],2))
"""

# todo: program: other solutions
# hw: program: https://www.codingninjas.com/codestudio/problems/cooking-ninjas_1164174
# n cooks numbered from 0 to n-1
# cook has rank between 1 and 10
# cook with rank r can prepare 1 dish in first r minutes, 1 more in next 2r, 1 more in next 3r and so on - only complete dishes
# 2g: if cook with rank2 has 12 minutes, he can make 2+4+6 mins = 3 dishes same for 13 minutes as only complete dishes
# question:
# order of M dishes to be completed as soon as possible
# array rank of size N for rank of each cook
# find minimum time required
# one dish y one cook only
# cooks can work simultaneously
# eg:N=4
#          0 1 2 3
# ranks = [1,2,3,4]
# M = 11
# ans = 12 mins
# 1--> 1+2+3+4, 2--> 2+4+6, 3-->3+6, 4->4,8
# eg: [10] ans 1 dish - 10 mins
# eg: [1,2,3,4] -> 10 dishes -> 12 mins
# eg: [1 1 1 1 1 1 1 1] -> 8 dishes -> 1 min
# my logic:
# start=0
# end=time taken by lowest ranked chef to cook all dishes
# mid
# check if mid is possible ans, if yes, check for smaller ans, if not check for bigger ans
# to check possible, allocate dishes to each cook within the given ans and see if they fit in
"""
def calculate_time_for_one_chef(rank, no_of_dishes):
    ans = 0
    for i in range(1, no_of_dishes+1):
        ans = ans + (i*rank)
    return ans
def find_minimum_time_to_cook(ranks, M):
    start = 0
    end = calculate_time_for_one_chef(max(ranks), M)  # not exceeding int range as per given inputs
    ans = 0
    while start <= end:
        mid = start + ((end-start)//2)
        if check_possible_solution(ranks, M, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
def check_possible_solution(ranks, no_of_dishes, max_time_per_chef):
    chef_number = 1
    chef_time = 0
    chef_dishes = 0
    completed_dishes = 0
    while completed_dishes < no_of_dishes:
        if chef_time + ((chef_dishes + 1) * ranks[chef_number-1]) <= max_time_per_chef:
           chef_time += ((chef_dishes + 1) * ranks[chef_number-1])
           chef_dishes += 1
           completed_dishes += 1
        else:
            chef_number += 1
            if chef_number > len(ranks):
                return False
            chef_time = 0
            chef_dishes = 0
    return True
print(find_minimum_time_to_cook([1,2,3,4], 11))  # 12
print(find_minimum_time_to_cook([10], 1))  # 10
print(find_minimum_time_to_cook([1,2,3,4], 10))  # 12
print(find_minimum_time_to_cook([1,1,1,1,1,1,1,1], 8))  # 1
"""

# todo: program: other solutions
# todo: try submitting on spoj without TLE
# hw: program: https://www.spoj.com/problems/EKO/
# wood to be chopped = m metres
# cut a single row of trees only
# machine params - height H, cuts all tree parts higher than H
# dont cut more wood than necessary
# set height as high as possible
# question:
# heights of trees and metres to cut in total given
# return max height of saw to cut minimum metres >= given metres
# my logic:
# start = 0, end=max(arr), mid, stop when start and end cross
# check if possible, if yes, check greater ans i.e. start = mid + 1, else check smaller ans i.e. end = mid - 1
# to check if possible, for each tree, save metres that will be cut off, if we run out, return False, if fits, return True
"""
def find_max_machine_height(tree_heights, metres_to_cut):
    start = 0
    end = max(tree_heights)
    ans = -1
    while start <= end:
        mid = start + ((end-start)//2)
        if is_possible_solution(tree_heights, metres_to_cut, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans
def is_possible_solution(tree_heights, metres_to_cut, height_of_machine):
    metres_cut_so_far = 0
    for i in range(len(tree_heights)):
        if tree_heights[i] <= height_of_machine:
            metres_that_can_be_cut_for_this_tree = 0
        else:
            metres_that_can_be_cut_for_this_tree = tree_heights[i] - height_of_machine
        metres_cut_so_far += metres_that_can_be_cut_for_this_tree
        if metres_cut_so_far >= metres_to_cut:
            return True
    return False
print(find_max_machine_height([20,15,10,17],7))  # 15
print(find_max_machine_height([4,42,40,26,46],20))  # 36
"""

# todo: program: other solutions
# hw: program: https://www.hackerrank.com/challenges/beautiful-triplets/problem
# array a - sorted
# a triplet (a[i],a[j],a[k]) is beautiful if:
# they lie in sequence (with gaps)
# their difference should be same ans should be d
# eg:
# arr=[2,2,3,4,5]
# d=1
# ans indexes: [0,2,3] [1,2,3] [2,3,4]
# return no of beautiful triplets
# eg: [1, 2, 4, 5, 7, 8, 10], 3
# ans: 3
# my logic: keep counter i.e. map of counts, for each unique element i.e. from set multiply its count with count of +d and count of +2d
# my logic: this covers duplicate elements also
"""
from collections import Counter
def count_beautiful_triplets(arr, d):
    counter = Counter(arr)
    count = 0
    for item in set(arr):
        count += (counter[item] * counter[item+d] * counter[item+d+d])
    return count
print(count_beautiful_triplets([2,2,3,4,5], 1))  # 3
print(count_beautiful_triplets([1, 2, 4, 5, 7, 8, 10], 3))  # 3
"""
