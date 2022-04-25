# program: positive or negative
"""
a = int(input("enter a "))
print(f"value of a is {a}")
if a > 0:
    print("a is positive")
else:
    print("a is 0 or negative")
"""

# program: a is bigger or smaller than b
"""
a = int(input("enter a "))
b = int(input("enter b "))
if a > b:
    print("a is bigger")
if b > a:
    print("b is bigger")
"""

# program: positive or negative or 0
"""
n = int(input("enter n "))
if n > 0:
    print("positive")
else:
    if n < 0:
        print("negative")
    else:
        print("0")
"""

# program: positive or negative or 0 with elif
"""
n = int(input("enter n "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("0")
"""

# hw: program: lower case or upper case or numeric
"""
c = input("enter c ")
ascii_value = ord(c)
if ord(c) >= ord("a") and ord(c) <= ord("z"):
    print("lower")
elif ord(c) >= ord("A") and ord(c) <= ord("Z"):
    print("upper")
elif ord(c) >= ord("0") and ord(c) <= ord("9"):
    print("numeric")
else:
    print("unknown")
"""

# program: while loop
"""
n = int(input("enter n "))
i = 1
while i <= n:
    print(i)
    i += 1
"""

# program: sum of 1 to n
"""
n = int(input("enter n "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
"""

# todo: math: how n(n+1)/2 works for sum of 1 to n
# program: sum of 1 to n - logic: sum of 1 to n: n(n+1)/2 - eg: sum of 1 to 5 = 5*6/2

# hw: program: find sum of all even numbers till n
"""
n = int(input("enter n "))
sum = 0
i = 2
while i <= n:
    sum = sum + i
    i = i + 2
print(sum)
"""

# hw: program: farhenheit to celsius table - logic: c = (f-32) * 5/9
"""
start = int(input("enter start "))
end = int(input("enter end"))
step = int(input("enter step"))
print("f\tc")
f = start
while f <= end:
    c = (f-32)*(5/9)
    print(f"{f}\t{c}")
    f = f + step
"""

# program: prime or not
"""
n = int(input("enter n "))
i = 2
prime = False
while i < n:
    if n % i == 0:
        print(f"not prime for {i}")
    else:
        print(f"prime for {i}")
    i = i + 1
"""

# program: pattern - logic: row=col=given num, data = *
# ****
# ****
# ****
# ****
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        print("*", end=" ")
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: row=col=given num, data=rownum
# 111
# 222
# 333
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        print(r, end='')
        c = c + 1
    print()
    r = r + 1
"""
