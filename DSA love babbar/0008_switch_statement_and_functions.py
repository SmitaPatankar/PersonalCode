# switch case program
# print whether number is one or two or default
# if number if 2, print whether character is a (nested)
"""
num = 2
char = "a"
if num == 1:
    print("first")
elif num == 2:
    print("second")
    if char == "a":
        print("a")
else:
    print("default")
"""

# homework
# switch case inside infinite while loop to check if number is one or two or default
# come out usinf exit()
"""
num = 1
while True:
    if num == 1:
        print("one")
        exit()
    elif num == 2:
        print("two")
        exit()
    else:
        print("default")
        exit()
"""

# switch case calculator program
"""
a = int(input("enter a number "))
b = int(input("enter another number "))
operation = input("enter an operation ")
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "//":
    print(a // b)
elif operation == "%":
    print(a % b)
else:
    print("please enter a valid operation")
"""

# homework
# program for calculating number of diff amount notes for total money
# eg:
# notes = 100,50,20,10
# total = 1330
# needs 13 * 100, 1 * 20, 1 * 10
"""
total = int(input("enter total "))
if total >= 100:
    print(f"number of notes of 100 rs = {total // 100}")
    total = total % 100
if total >= 50:
    print(f"number of notes of 50 rs = {total // 50}")
    total = total % 50
if total >= 20:
    print(f"number of notes of 20 rs = {total // 20}")
    total = total % 50
if total >= 10:
    print(f"number of notes of 10 rs = {total // 10}")
    total = total % 50
else:
    print("amount is too low for notes")
"""

# functions
"""
- non bulky
- non buggy
- readable
- has signature i.e. what it accepts and returns and body i.e. task
"""

# function program - power of one number to other
"""
def power(num1, num2):
    ans = 1
    for i in range(num2):
        ans = ans * num1
    return ans
a = int(input("enter a "))
b = int(input("enter b "))
print(power(a, b))
"""

# function program - even odd
"""
def is_even(a):
    if a & 1:
        return False
    return True  # else
n = int(input("enter a number "))
if is_even(n):
    print("even")
else:
    print("odd")
"""

# function program for nCr i.e. (n!/(n-r)!)/r!
"""
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans
def ncr(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))
n = int(input("enter n "))
r = int(input("enter r "))
print(ncr(n, r))
"""

# function program for counting
"""
def count(n):
    for i in range(1, n+1):
        print(i, end=" ")  # returns None
n = int(input("enter a number "))
count(n)
"""

# function program to check if prime
"""
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
n = int(input("enter a number "))
if is_prime(n):
    print("prime")
else:
    print("not prime")
"""

# function call stack
"""
LIFO - last in first out

inner function (3.push) (4.pop)
outer function (2. push)(5.pop)
main function  (1. push)(6.pop)
"""

# homework
# mathematical concept for arithmetic progression - revisit
# function program - arithmetic progression (3 * n + 7)
"""
def arithmetic_progression(n):
    return (3 * n) + 7
n  = int(input("enter a number "))
print(arithmetic_progression(n))
"""

# homework
# function program for total number of set bits in number 1 and number 2
# set bits = 1 bits
"""
def count_set_bits_in_num(n):
    count = 0
    while n != 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count
def count_set_bits_in_two_nums(a, b):
    return count_set_bits_in_num(a) + count_set_bits_in_num(b)
a = int(input("enter a "))
b = int(input("enter b "))
print(count_set_bits_in_two_nums(a, b))
"""

# homework
# function program for nth fibonacci number
"""
def fib(n):
    if n < 1:
        print("enter a valid number")
        exit()
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for i in range(3, n+1):
        next_num = a + b
        a = b
        b = next_num
    return b
n = int(input("enter a number "))
print(fib(n))
"""

# pass by object reference
# outside there is one box that has content
# inside there is another box that has same content
# if inside box is reassigned another value, it won't reflect on the outside box
"""
def m(n):
    n = n + 1
    print(n)
n = int(input("enter a number "))
print(n)
m(n)
print(n)
"""
