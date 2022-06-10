# recursion
"""
base case mandatory to avoid stackoverflow
recursive relation mandatory
processing optional

like going home one step at a time
then do that recursively until we reach i.e. until entire problem gets solved
decide when to stop also i.e. when we reach home
"""

# program - recursion - reach home
"""
def move(src, dest):
    print(f"source={src} destination={dest}")
    if src == dest:
        print("reached")
        return
    src += 1
    move(src, dest)
move(1,10)
"""

# todo: math: principle of mathematic induction - prove base case i.e. f(0or1) true - assume f(k) true - prove f(k+1) is true
# tbd: optimize using DP
# program - recursion - fibonacci number - https://leetcode.com/problems/fibonacci-number/
# nth number is n-1th number + n-2th number
# stop when n <= 1 in which case fib number is same as index
"""
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))
"""

# hw: program: fibonacci number using for loop
"""
def fib(n):
    a = 0
    b = 1
    ans = 0
    for i in range(n+1):
        if i == 0:
            ans = a
        elif i == 1:
            ans = b
        else:
            ans = a+b
            a = b
            b = ans
    return ans
print(fib(10))
"""

# todo: build intuition
# tbd: optimize using dp
# program: ways to reach n stairs - https://www.codingninjas.com/codestudio/problems/count-ways-to-reach-nth-stairs_798650
# 0th at start - go to nth - at a time we can climb either one stair or 2 stairs
# tell distinct ways of reaching
# logic: sum up ways of reaching previous and its previous stairs recursively
"""
def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return count_ways(n-1) + count_ways(n-2)
print(count_ways(5))
"""

# program - say digits
# for 412 - say four one two
# f(0) --> return
# f(4) --> print(4)
# f(41) --> print(1)
# f(412) --> print(2)
# 
# stack over
"""
def say(n, arr):
    if n == 0:
        return
    digit = n % 10
    n = n // 10
    say(n, arr)
    print(arr[digit])
say(4102, ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
"""
