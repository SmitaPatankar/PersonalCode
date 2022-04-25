# switch statement details
"""
- to avoid if elif...elif else
- not applicable in python
"""

# program: switch
"""
num = 2
if num == 1:
    print("first")
elif num == 2:
    print("second")
else:
    print("default")
"""

# keywords details
"""
- break - come out of loop
- continue - skip this iteration and go to next
- exit() - exit the program
"""

# program: switch case calculator
# a, b, operation is given
# return output
# * / + - %
# int output
"""
def calculator(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b
    elif op == "%":
        return a % b
    else:
        return "invalid operation"
print(calculator(102,10,"%"))
"""

# todo: program: other solutions
# hw: for given amount of money, show number of 100,50,20,1 notes needed
# logic: divide by largest number and so on, quotient is number of notes and remainder is money for next note
"""
def notes_calculator(money):
    for note_value in [100,50,20,1]:
        no_of_notes = money // note_value
        money = money % note_value
        print(f"no of {note_value} rs notes is {no_of_notes}")
notes_calculator(130)
"""

# functions details
"""
- to avoid writing same lines repeatedly and create bulky, buggy and non readable code
- function has well defined task for taking i/p and giving o/p
- write once, use many times
"""

# program: function for power of 2 numbers
"""
def power(a,b):
    ans = 1
    for i in range(b):
        ans = ans * a
    return ans
a = int(input("enter a "))
b = int(input("enter b "))
ans = power(a,b)
print(ans)
"""

# program: even odd - logic: &1 should be 1
"""
def is_even(n):
    if n & 1 == 1:
        return 0
    else:
        return 1
num = int(input("enter num"))
if is_even(num):
    print("even")
else:
    print("odd")
"""

# todo: math: ncr derivation
# program: ncr - logic: ncr = n!/(n-r)!r! - logic: 0! = 1
"""
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    print(f"factorial of {n} is {ans}")
    return ans
def ncr(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))
n = int(input("enter n "))
r = int(input("enter r "))
print(ncr(n, r))
"""

# program: counting
"""
# signature
def print_counting(n):
    # body
    for i in range(1,n+1):
        print(i)
# call
print_counting(int(input("enter n ")))  # outside scope not accessible inside function
"""

# program: is prime
"""
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
n = int(input("enter n "))
if is_prime(n):
    print("prime")
else:
    print("not prime")
"""

# function call stack details
"""
- like stack of plates
- add one over other
- remove in reverse order
- added as:
    factorial()
    ncr()
    main
- removed as:
    factorial - gives ans below
    ncr - gives ans below
    main - utilizes ans - empty stack - returns and exits
"""

# hw: program: arithmetic progression is 3 * n + 7, n given, we have to give nth term
"""
def arithmetic_progression(n):
    return 3 * n + 7
print(arithmetic_progression(3))
"""

# hw: program: a and b given, give total number of set bits i.e. 1 bits in a & b
# eg: 2,3 i.e. 10,11 i.e. 3 set bits
"""
def set_bits(a,b):
    ans = 0
    for num in (a,b):
        while num != 0:
            bit = num & 1
            if bit == 1:
                ans += 1
            num = num >> 1
    return ans
print(set_bits(3,5))
"""

# todo: program: other solutions
# hw: program: fibonacci series nth element when n is given
"""
def fib(n):
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(3,n+1):
        c = a + b
        a = b
        b = c
    return c
print(fib(5))
"""

# todo: python: pass by value and reference
# pass by value - copied to function
# tbd: pass by reference
"""
def dummy(n):
    print(id(n))  # same
    print(n)  # 5
    n = n + 1
    print(id(n))  # diff
    print(n)  # 6
n = 5
print(id(n))  # same
print(n)  # 5
dummy(n)
print(id(n))  # same
print(n)  # 5
"""
