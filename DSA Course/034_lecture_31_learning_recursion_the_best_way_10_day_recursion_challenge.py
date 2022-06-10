# recursion
"""
function calls itself directly or indirectly(via other function call)

when bigger problem's solution relies on same type of smaller problem's solution

eg:
2^4 = 2 * 2 ^ 3 = 2 * 8 = 16
2^3 = 2 * 2 ^ 2 = 2 * 4 = 8
2^2 = 2 * 2 ^ 1 = 2 * 2 = 4
2^1 = 2 * 2 ^ 0 = 2 * 1 = 2
2^0 = 1
recursive relation:
2^n = 2 * 2^(n-1)
f(n) = 2 * f(n-1)

eg:
5! = 5 * 4! = 5 * 24 = 120
4! = 4 * 3! = 4 * 6 = 24
3! = 3 * 2! = 3 * 2 = 6
2! = 2 * 1! = 2 * 1 = 2
1! = 1 * 0! = 1 * 1 = 1
0! = 1
recursive relation:
n! = n * (n-1)!
f(n) = n * f(n-1)

base case is the last case for which we already know the ans and dont have to go any further

needs recursive relation and base case
base case should always be returned

without base case, program will keep looping forever and result in stack overflow i.e. full memory
function call stack has entries like main -> factorial(5) -> factorial(4) etc

can have processing part also i.e. printing, addition etc

when recursion comes after processing it is called tail recursion
when recursion comes before processing it is called head recursion

recursion tree to picturise flow
"""

# program - recursion - factorial
"""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(int(input("n-->"))))
"""

# program - recursion - power of 2
"""
def power_of_two(n):
    if n == 0:
        return 1
    return 2 * power_of_two(n-1)
print(power_of_two(3))
"""

# program - tail recursion - print reverse counting
"""
def reverse_counting(n):
    if n == 0:
        return
    print(n)
    reverse_counting(n-1)
reverse_counting(5)
"""

# program - head recursion - print counting
# r(5)
# r(4) print(5) --> 5
# r(3) print(4) --> 4
# r(2) print(3) --> 3
# r(1) print(2) --> 2
# r(0) print(1) --> 1
# r(0) --> nothing
"""
def counting(n):
    if n == 0:
        return
    counting(n-1)
    print(n)
counting(5)
"""

# hw: recursion: read and solve: https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118522/offering/1380913

# hw: program - nth fibonacci - recursion
"""
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)
print(fib(5))
"""

# hw: program - recursion - check if array is sorted
# check_sorted([1,2,3,4],0) BC F res1 = True & ? True - True
# check_sorted([1,2,3,4],1) BC F res1 = True & ? True - True
# check_sorted([1,2,3,4],2) BC F res1 = True & ? True - True
# check_sorted([1,2,3,4],3) BC T True
# -------------------------------------------------------------
# check_sorted([6,3,2,1],0) BC F res1 = False & ? True - False
# check_sorted([6,3,2,1],1) BC F res1 = False & ? True - False
# check_sorted([6,3,2,1],2) BC F res1 = True & ? True - True
# check_sorted([6,3,2,1],3) BC T True
"""
def check_sorted(a, i):
    if i == len(a) - 1:
        return True
    res1 = a[i] < a[i+1]
    res2 = check_sorted(a, i+1)
    return res1 and res2
print(check_sorted([1,2,3,4], 0))
print(check_sorted([6,3,1,2], 0))
"""

# hw: program: recursion: family structure: https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118522/offering/1380914
# aakash's family
# male gives male child first then girl child
# female gives female child first and then male child
# find kth child in his nth generation
# eg:
# m
# m           f
# m f*        f m
# second child in 3rd generation
# first m is aakash
# every child has 2 children
# --------------------------------------------
# n=3 find for n=2 and process further i.e. ["male","male","female"] process --> ["male","female"] for previous level process --> ["male","male","female","male","female","female","male"]
# n=2 find for n=1 and process further i.e. ["male"] --> ["male"] for previous level and process further - i.e. make it ["male","male","female"]
# n=1 return ["male"]
# ---------------------------------------------
# logic: if k == 1 or n == 1 Male
# else: get k/2th person from previous level and then calculate based on whether k is its first child or second and whether it is male or female
"""
def kth_child_in_nth_generation(n, k):
    if k == 1 or n == 1:
        print("parent generation is nothing parent position is nothing")
        ans = "Male"
        print(f"child {k} for generation {n} is {ans}")
        return ans
    parent_generation = n-1
    parent_position = (k+1) // 2
    print(f"parent generation is {parent_generation} parent position is {parent_position}")
    parent = kth_child_in_nth_generation(parent_generation, parent_position)
    if k == parent_position * 2:
        ans = "Female" if parent == "Male" else "Male"
        print(f"child {k} for generation {n} is {ans}")
        return ans
    ans = parent
    print(f"child {k} for generation {n} is {ans}")
    return ans
n = 2
k = 2
print(f"final - child {k} for generation {n} is {kth_child_in_nth_generation(n, k)}")  # female
print()
n = 3
k = 4
print(f"child {k} for generation {n} is {kth_child_in_nth_generation(n, k)}")  # male
"""

# hw: program: recursion: nth term of gp - https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118522/offering/1380915
# todo: try submitting on code studio later along with mod
# first term a
# common ratio r
# integer n
# find nth term of gp series
# logic: gp series: a*(r^0) + a*(r^1)+ a*(r^2) + .... + a*(r^n-1)
# return ans as modulo 10^9 + 7
# eg: n=5, a=3, r=2
# ans = 3*(2^4) + 3*(2^3) + 3*(2^2) + 3*(2^1) + 3*(2^0)
# -----------------------------
# nth_gp_term(n=5,a=3,r=2, sum=0)
# 5th term = 3(2^4) + nth_gp_term(n=4,a=3,r=2, sum=0) --> 48 + 45 = 93
# 4th term = 3(2^3) + nth_gp_term(n=3,a=3,r=2, sum=0) --> 24 + 21 = 45
# 3rd term = 3(2^2) + nth_gp_term(n=2,a=3,r=2, sum=0) --> 12 + 9 = 21
# 2nd term = 3(2^1) + nth_gp_term(n=1,a=3,r=2, sum=0) --> 6 + 3 --> 9
# 1st term = a --> 3
"""
def nth_gp_term(n, a, r):
    if n == 1:
        print(f"term number {n} is {a}")
        return a
    ans = a*(r**(n-1)) + nth_gp_term(n-1, a, r)
    print(f"term number {n} is {ans}")
    return ans
print(nth_gp_term(n=3,a=1,r=2))
"""

# hw: program: recursion: print series - https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118522/offering/1380916
# 2 integers n and k
# subtract k fron n until it becomes 0 or negative then add k until it becomes n
# without loop
"""
def solve(n, k, ans):
    ans.append(n)
    if n <= 0:
        return ans
    else:
        solve(n-k,k,ans)
        ans.append(n)
def print_series(n, k):
    ans = []
    solve(n,k,ans)
    return ans
print(print_series(10,2))
"""

# hw: program: recursion: return subsets sum to k - https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118522/offering/1380917
# arr of size n
# int k
# return subsets with sum k
# elements in subset should be sequential as per index
# order of subsets doesnt matter
# eg: {2, 4, 6} for sum 6
# subsets {}, {2}, {4}, {6}, {2, 4}, {2, 6}, {4, 6}, {2, 4, 6}
# ans {2, 4} and {6}
"""
def subsets(arr, n, k, ans):
    if n == 1:
        current_subsets = [[], arr]
        for current_subset in current_subsets:
            if sum(current_subset) == k:
                ans.append(current_subset)
        return current_subsets
    else:
        previous_subsets = subsets(arr[1:], n-1, k, ans)
        current_subsets = []
        for previous_subset in previous_subsets:
            current_subset = [arr[0]] + previous_subset
            current_subsets.append(current_subset)
            if sum(current_subset) == k:
                ans.append(current_subset)
        current_subsets.extend(previous_subsets)
        return current_subsets
def find_subsets_that_sum_to_k(arr, n, k) :
    ans = []
    subsets(arr, n, k, ans)
    return ans
print(find_subsets_that_sum_to_k([0,1,2,3,4],5,6))
"""

# hw: program - tower of hanoi - recursion - https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118522/offering/1380918
# 3 rods numbered 1 to 3
# n disks initially on first rod - largest disk at bottom
# move them to any one of the other rod in less than 2^n moves
# move one disk in one move
# cant place larger on smaller
# can only move top disk
# assume disk at ith position has size 1 and so on
# return set of sets with from and to positions
# logic:
# everytime of think that base disk is to be moved from start to end that means above all disks need to be moved from start to other i..e recursive call, then move base from start to end, then again move rest from other to end
# stop when only 1 disk is base
# other is 6-start-end coz 1+2+3
"""
def move_disks(n, start, end, moves):
    if n == 1:
        # print(f"moving top 1 disk from rod {start} to {end}.................")
        moves.append([start, end])
    else:
        other = 6-start-end
        # print(f"need to move top {n-1} disks from rod {start} to {other} first and then need to move bottom {n} disk from {start} to {end}")
        move_disks(n-1, start, other, moves)
        moves.append([start, end])
        # print(f"moving bottom {n} disk from {start} to {end}######################")
        move_disks(n-1, other, end, moves)
def tower_of_hanoi(n):
    moves = []
    # print(f"problem is to move 5 disks from rod 1 to 3")
    move_disks(n,start=1,end=3, moves=moves)
    return moves
# print(tower_of_hanoi(n=5))
"""
