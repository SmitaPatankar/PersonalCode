# https://www.codingninjas.com/codestudio/contests/love-babbar-contest-l

# todo: program: other solutions
# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-l/problems/16513
# R rows
# C columns
# draw diamond shape of size S in each cell of grid
# /\ represent borders of diamond
# o represents space inside diamond
# e represents rest of the space of diamond
#
# r, c and s are given
# rows and cols are from 1 to 100
# size is between 1 to 10
# time limit is 1 sec
#
# eg: r=1,c=1,s=2
# e/\e
# /oo\
# \oo/
# e\/e
#
# eg: r=3,c=1,s=2
# e/\e
# /oo\
# \oo/
# e\/e
# e/\e
# /oo\
# \oo/
# e\/e
# e/\e
# /oo\
# \oo/
# e\/e
#
# eg: r=4,c=4,s=1
#
# eg: r=2,c=5,s=2
#
# eg: r=1,c=1,s=3
"""
def print_the_diamond(r,c,s):
    for row in range(r):
        for i in range(s,0,-1):
            pattern = f"{'e'*(i-1)}/{'o'*(2*(s-i))}\\{'e'*(i-1)}"
            # pattern = "%s/%s\%s" % ('e'*(i-1), 'o'*(2*(s-i)), 'e'*(i-1))
            # pattern = 'e'*(i-1) + "/" + 'o'*(2*(s-i)) + "\\" + 'e'*(i-1)
            for col in range(c):
                print(pattern,end='')
            print()
        for i in range(s,0,-1):
            pattern = f"{'e'*(s-i)}\\{'o'*(2*(i-1))}/{'e'*(s-i)}"
            # pattern = f"%s\%s/%s" % ('e'*(s-i), 'o'*(2*(i-1)), 'e'*(s-i))
            # pattern = 'e'*(s-i) + "\\" + 'o'*(2*(i-1)) + "/" + 'e'*(s-i)
            for col in range(c):
                print(pattern,end='')
            print()
print_the_diamond(2,3,5)
"""

# todo: program: learn and code your own efficient sorting algorithm that doesn't lead to TLE
# todo: program: other solutions
# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-l/problems/14804
# n number of apples
# cost of apples is given in arr
# buy all apples
# coupon to pay for m-1 apples and get m apples i.e. cheapest one free
# find minimal total coins required to buy all apples, use coupon wisely
#
# eg:
# n apples i.e. 5
# arr = [5,2,4,1,3]
# m = 3
# ans: 12 coz we'll select 5,4,3 to get cheapest among them i.e. 3 for discount which is max discount when choosing 3 apples, so remaining cost for all apples is 12
#
# apples can be upto 10**4
# cost can be upto 10**9
#
# my logic: sort descending and we'll get the m-1th apple free so deduct that from sum
"""
def apple_and_coupon(n,m,arr):
    arr.sort(reverse=True)
    sum = 0
    for i in range(n):
        if i != m - 1:
            sum = sum + arr[i]
    return sum
print(apple_and_coupon(2,2,[3,2]))
print(apple_and_coupon(4,2,[2,3,1,5]))
"""

# todo: program: other solutions
# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-l/problems/15017
# array r
# length n
# split it into 3 parts so that each number is in single part only
# each part should be contiguous as per original array
# part can empty
# sum of each part is s1, s2, s3
#
# conditions to fulfill:
# s1 == s3
# s1 must be max possible amongst all possible ways
#
# eg:
# n=5
# arr=[5,2,4,1,4]
#
# 1<= ‘N’<= 10^4
# 1 <= ‘ARR[i]’ <= 10^6
#
# my logic:
# two pointer approach as we care about left sum and right sum
# start left from 0 and left_sum from 0th sum, start right from n-1 and right sum from n-1th sum
# if sums are same, increment both and increment both sums
# else: increment smaller one
# end when start < end
# don't check equal because one element can e in one part only
"""
def three_way_split(n, arr):
    left_pointer = 0
    right_pointer = n-1
    left_sum = arr[left_pointer]
    right_sum = arr[right_pointer]
    ans = 0
    while left_pointer < right_pointer:
        if left_sum == right_sum:
            ans = left_sum
            left_pointer += 1
            right_pointer -= 1
            left_sum += arr[left_pointer]
            right_sum += arr[right_pointer]
        elif left_sum < right_sum:
            left_pointer += 1
            left_sum += arr[left_pointer]
        else:
            right_pointer -= 1
            right_sum += arr[right_pointer]
    return ans
print(three_way_split(4,[2,3,1,5]))
"""

# todo: program: other solutions
# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-l/problems/14463
# we have b candies
# and n friends
# each friend has their demand
# find maximum candies x such that all demand <= x can be fulfilled and total wont exceed available candies
#
# eg:
# 20 candies
# 3 friends - 1 2 3, 4 2 3,1 10 2
# ans: 9 i.e. 123,423,12
# total: 18 within 20
#
# my logic:
# start = 0
# end = no of available candies
# mid
# stop when start <= end
# if possible, check greater, else check lesser
# to check if possible, try to give all demands <= mid
# first number in friend demands is number of demands
"""
def find_max_x(friends_demands, available_candies):
    start = 0
    end = available_candies
    ans = -1
    while start <= end:
        mid = start + (end-start)//2
        if is_possible_solution(friends_demands, available_candies, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans
def is_possible_solution(friend_demands, available_candies, max_candy):
    candies_used = 0
    for friend_number in range(len(friend_demands)):
        for demand_number in range(1, friend_demands[friend_number][0]+1):
            if friend_demands[friend_number][demand_number] <= max_candy:
                candies_used += friend_demands[friend_number][demand_number]
                if candies_used > available_candies:
                    return False
    return True
print(find_max_x([[3,1,2,3],[3,4,2,3],[3,1,10,2]], 20))
"""
