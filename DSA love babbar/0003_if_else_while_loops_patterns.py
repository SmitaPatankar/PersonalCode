# condition programs
"""
a = int(input("enter a "))
if a > 0:
    print("a is +ve")
elif a < 0:
    print("a is -ve")
else:
    print("a is 0")
"""

# homework
# print whether character is lower/upper/digit
"""
chr = input("enter a character ")
ord_chr = ord(chr)
if ord_chr in range(ord("a"), ord("z")+1):
    print("lower")
elif ord_chr in range(ord("A"), ord("Z")+1):
    print("upper")
elif ord_chr in range(ord("0"), ord("9")+1):
    print("digit")
"""

# while loop program
# print numbers from 1 to n
"""
n = input("enter a number ")
i = 1
while i <= int(n):
    print(i, end=" ")
    i += 1
"""

# sum of 1 to n
"""
n = int(input("enter a number "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)
"""

# homework
# sum of even numbers from 1 to n
"""
n = int(input("enter a number "))
sum = 0
i = 2
while i <= n:
    sum = sum + i
    i = i + 2
print(sum)
"""

# homework
# farenheit to celsius table
"""
n = int(input("enter a number "))
f = 32
while f <= n:
    c = (f - 32) * 5/9
    print(f"{f} Fahrenheit = {c} degree celsuis")
    f += 10
"""

# prime or not prime
"""
n = int(input("enter a number "))
i = 2
prime = True
while i < n:
    if n % i == 0:
        print(f"not prime for {i}")
    else:
        print(f"prime for {i}")
    i += 1
"""

# patterns program
# * * * *
# * * * *
# * * * *
# * * * *
"""
# rows = columns, data = *
n = int(input("enter a number "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1
"""

# 1 1 1
# 2 2 2
# 3 3 3
"""
# rows = columns, data = row num
n = int(input("enter a number "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i, end="")
        j = j + 1
    print()
    i = i + 1
"""