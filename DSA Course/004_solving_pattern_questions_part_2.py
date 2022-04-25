# program: pattern - logic: row=col=given num, data=colnum
# 1234
# 1234
# 1234
# 1234
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        print(c, end='')
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: row=col=given num, data=reverse of column numbers i.e. n-c+1
# 321
# 321
# 321
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        print(n-c+1, end='')
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: row=col=given num, data=starts from 1 and continues till last element
# 123
# 456
# 789
"""
n = int(input("enter n "))
r = 1
seq = 1
while r <= n:
    c = 1
    while c <= n:
        print(seq, end='')
        seq = seq + 1
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, cols=rownum, data=*
# *
# **
# ***
# ****
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= r:
        print("*",end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, cols=rownum, data=rownum
# 1
# 22
# 333
# 4444
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= r:
        print(r,end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, cols=rownum, data=start from 1 and continue till last element
# 1
# 23
# 456
# 78910
"""
n = int(input("enter n "))
r = 1
seq = 1
while r <= n:
    c = 1
    while c <= r:
        print(seq,end = " ")
        seq = seq + 1
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, cols=rownum, data=start from rownum and continue
# 1
# 23
# 345
# 4567
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    seq = r
    while c <= r:
        print(seq,end = " ")
        seq = seq + 1
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, cols=rownum, data=start from rownum and continue - without saving data explicitly - logic: data=r+c-1
# 1
# 23
# 345
# 4567
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= r:
        print(r+c-1,end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, cols=rownum, data=start from rownum and minus - without saving data explicitly - logic: data=r-c+1
# 1
# 21
# 321
# 4321
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= r:
        print(r-c+1,end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=colcount=givennum, data = A(97) for first row and so on - without saving value - data = A + rownum - 1
# AAA
# BBB
# CCC
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        print(chr(ord("A")+r-1),end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=colcount=givennum, data = A(97) and continue for row - without saving value - data = A + colnum - 1
# ABC
# ABC
# ABC
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        print(chr(ord("A")+c-1),end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=colcount=givennum, data = A(97) and continue till last element
# ABC
# DEF
# GHI
"""
n = int(input("enter n "))
r = 1
seq = ord("A")
while r <= n:
    c = 1
    while c <= n:
        print(chr(seq),end = " ")
        seq = seq + 1
        c = c + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=colcount=givennum, data = start from rownum letter and continue A for first row start, B for 2nd row start etc, A+r+c-2
# ABC
# BCD
# CDE
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n:
        print(chr(ord("A")+r+c-2),end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=colcount=givennum, data = start from rownum letter and continue A for first row start, B for 2nd row start etc, save value explicitly, start = A+r-1
# ABC
# BCD
# CDE
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    seq = ord("A")+r-1
    while c <= n:
        print(chr(seq),end = " ")
        seq = seq + 1
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, colcount=rownum, data = A for first row, b for 2nd so on, A + r -1
# A
# BB
# CCC
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= r:
        print(chr(ord("A")+r-1),end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, colcount=rownum, data = start from A and go on till last element
# A
# BC
# DEF
"""
n = int(input("enter n "))
r = 1
seq = 0
while r <= n:
    c = 1
    while c <= r:
        print(chr(ord("A")+seq),end = " ")
        seq = seq + 1
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, colcount=rownum, data = start from A for first row, b for second - A+r+c-2
# A
# BC
# CDE
# DEFG
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= r:
        print(chr(ord("A")+r+c-2),end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, colcount=rownum, data = start from D for first row, c for second = A+n-r+c-1
# D
# CD
# BCD
# ABCD
# below logic or note down start of row as A+n-1 and keep decrementing for that row
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= r:
        print(chr(ord('A')+n-r+c-1),end = " ")
        c = c + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rowcount=givennum, colcount=rownum, data = n-r spaces and rownum stars, 2 loops
#    *
#   **
#  ***
# ****
"""
n = int(input("enter n "))
r = 1
while r <= n:
    space = n-r
    while space >= 1:
        print(" ", end="")
        space = space - 1
    star = 1
    while star <= r:
        print("*", end="")
        star = star + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, colcount=n-r+1, data = *
# ****
# ***
# **
# *
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n-r+1:
        print("*", end="")
        c = c + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, colcount=n-r+1, data = rownum spaces, n-r+1 stars 2 loops
# ****
#  ***
#   **
#    *
"""
n = int(input("enter n "))
r = 1
while r <= n:
    space = r
    while space >= 1:
        print(" ", end="")
        space = space - 1
    star = 1
    while star <= n - r + 1:
        print("*", end="")
        star = star + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, colcount=n-r+1, data = rownum-1 spaces, n-r+1 rownumprint 2 loops
# 1111
#  222
#   33
#    4
"""
n = int(input("enter n "))
r = 1
while r <= n:
    space = r-1
    while space >= 1:
        print(" ", end="")
        space = space - 1
    data_col = 1
    while data_col <= n - r + 1:
        print(r, end="")
        data_col = data_col + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, colcount=rownum, data = n-r spaces and rownum times rownum print, 2 loops
#    1
#   22
#  333
# 4444
"""
n = int(input("enter n "))
r = 1
while r <= n:
    space = n-r
    while space >= 1:
        print(" ", end="")
        space = space - 1
    data_col = 1
    while data_col <= r:
        print(r, end="")
        data_col = data_col + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, colcount=n-r+1, data = rownum-1 spaces, n-r+1 value 2 loops, value=start fromrownum and continue,r+c-1
# 1234
#  234
#   34
#    4
"""
n = int(input("enter n "))
r = 1
while r <= n:
    space = r-1
    while space >= 1:
        print(" ", end="")
        space = space - 1
    data_col = 1
    while data_col <= n - r + 1:
        print(r+data_col-1, end="")
        data_col = data_col + 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: rowcount=givennum, colcount=rownum, data = n-r spaces and rownum times seq print, 2 loops, seq from 1 to forever
#    1
#   23
#  456
# 78910
"""
n = int(input("enter n "))
r = 1
seq = 1
while r <= n:
    space = n-r
    while space >= 1:
        print(" ", end="")
        space = space - 1
    data_col = 1
    while data_col <= r:
        print(seq, end="")
        seq = seq + 1
        data_col = data_col + 1
    print()
    r = r + 1
"""

# program: pattern - logic: rownum=givenum, data=n-r spaces, rownum worth value1, rownum-1 worth value2, value1=data_col, value2=r-1 upto 1, 3 loops
#    1
#   121
#  12321
# 1234321
"""
n = int(input("enter n "))
r = 1
while r <= n:
    space = n-r
    while space >= 1:
        print(" ", end="")
        space = space - 1
    data_col = 1
    while data_col <= r:
        print(data_col, end="")
        data_col = data_col + 1
    start = r-1
    while start >=1:
        print(start,end="")
        start = start - 1
    print()
    r = r + 1
"""

# hw: program: pattern - logic: 3 loops: rownum=givenum, 1: colcount=n-r+1 and value=1 and continue, 2: colcount=(r-1)*2,value=*, 3:value=n-r+1 to 1
# 1234554321
# 1234**4321
# 123****321
# 12******21
# 1********1
"""
n = int(input("enter n "))
r = 1
while r <= n:
    c = 1
    while c <= n-r+1:
        print(c,end='')
        c = c + 1
    c = (r-1)*2
    while c >= 1:
        print("*", end="")
        c = c - 1
    start = n-r+1
    while start >= 1:
        print(start, end='')
        start = start - 1
    print()
    r = r + 1
"""
