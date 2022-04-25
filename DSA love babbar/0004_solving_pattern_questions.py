# pattern programs
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
"""
# rows=columns=4 data=column number
n = int(input("enter a number "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1
"""

# 3 2 1
# 3 2 1
# 3 2 1
"""
# number of rows=no of cols=3, data=reverse of column number (n-j+1)
n = int(input("enter a number "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(n-j+1, end="")
        j = j + 1
    print()
    i = i + 1
"""

# 1 2 3
# 4 5 6
# 7 8 9
"""
# no of rows=no of columns=3, data=keep on incrementing
n = int("enter a number "))
i = 1
count = 1
while i <= n:
    j = 1
    while j <= n:
        print(count, end=" ")
        j = j + 1
        count = count + 1
    print()
    i = i + 1
"""

# *
# **
# ***
# ****
"""
# rows=4, columns=same as current row number, data=*
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= row:
        print("*", end="")
        col = col + 1
    print()
    row = row + 1
"""

# 1
# 22
# 333
# 4444
"""
# rows=4,columns=same as current row number, data=current row number
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= row:
        print(row, end="")
        col += 1
    print()
    row += 1
"""

# homework
# 1
# 2 3
# 4 5 6
# 7 8 9 10
"""
# rows=4, columns=same as row number, data = keep incrementing
n = int(input("enter a number "))
row = 1
count = 1
while row <= n:
    col = 1
    while col <= row:
        print(count, end=" ")
        count += 1
        col += 1
    print()
    row += 1
"""

# 1
# 2 3
# 3 4 5
# 4 5 6 7
# easy way
"""
# rows=4, columns=same as current row num, data=start with current row num and increment
n = input("enter a number ")
row = 1
while row <= n:
    col = 1
    count = row
    while col <= row:
        print(count, end=" ")
        count += 1
        col += 1
    print()
    row += 1
"""

# homework
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# hard way
"""
# rows=4, columns=same as current row num, data=start with current row num and increment
n = input("enter a number ")
row = 1
while row <= 4:
    col = 1
    while col <= row:
        print(row + col - 1, end=" ")
        col += 1
    print()
    row += 1
"""

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# hard way
"""
# row=4, columns=same as row num, data=start with current row num and decrement
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= row:
        print(row - col + 1, end=" ")
        col += 1
    print()
    row += 1
"""

# A A A
# B B B
# C C C
"""
# rows = cols = 3, data = A in first row, B in 2nd and 3 in 3rd
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= n:
        print(chr(ord("A")+row-1), end=" ")
        col += 1
    print()
    row += 1
"""

# homework
# A B C
# A B C
# A B C
"""
# rows=cols=3, data = begin with A in each row and increment
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= n:
        print(chr(ord("A")+col-1), end=" ")
        col += 1
    print()
    row += 1
"""

# homework
# A B C
# D E F
# G H I
"""
# rows=columns=3, data=start from A initially and keep incrementing
n = int(input("enter a number "))
row = 1
count = ord("A")
while row <= n:
    col = 1
    while col <= n:
        print(chr(count), end=" ")
        count += 1
        col += 1
    print()
    row += 1
"""

# homework
# A B C
# B C D
# C D E
# easy way
"""
# rows=cols=3, data=start first row with A and increment, 2nd with , 3rd with C
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    count = row
    while col <= n:
        print(chr(ord("A") + count - 1), end=" ")
        count += 1
        col += 1
    print()
    row += 1
"""

# homework
# A B C
# B C D
# C D E
# difficult way
"""
# rows=cols=3, data=start first row with A and increment, 2nd with , 3rd with C
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= n:
        print(chr(ord("A")+row+col-2), end=" ")
        col += 1
    print()
    row += 1
"""

# A
# B B
# C C C
"""
# rows=3, columns=same as current row num, data = A in first row, B in 2nd, C in third
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= row:
        print(chr(ord("A")+row-1), end=" ")
        col += 1
    print()
    row += 1
"""

# homework
# A
# B C
# D E F
# G H I F
"""
# rows=4, columns=same as current row num, data is start with A and keep incrementing
n = int(input("enter a number "))
row = 1
count = ord("A")
while row <= n:
    col = 1
    while col <= row:
        print(chr(count), end=" ")
        count += 1
        col += 1
    print()
    row += 1
"""

# A
# B C
# C D E
# D E F G
# hard way
"""
# rows=4, columns=same as row num, data = start with digit for row num and increment
n = int(input("enter a number "))
row = 1
while row <= n:
    col = 1
    while col <= row:
        print(chr(ord("A")+row+col-2), end=" ")
        col += 1
    print()
    row += 1
"""

# D
# C D
# B C D
# A B C D
# easy way
"""
# rows=4, columns=same as current row number, data=start first row with D and decrement, 2nd with C, 3rd with b, 4th with A
n = int(input("enter a number "))
row = 1
while row <= 4:
    col = 1
    count = ord("A") + n - row
    while col <= row:
        print(chr(count), end="")
        count += 1
        col += 1
    print()
    row += 1
"""

# homework
# D
# C D
# B C D
# A B C D
# difficult way
"""
# rows=4, columns=same as current row number, data=start first row with D and decrement, 2nd with C, 3rd with b, 4th with A
n = int(input("enter a number "))
row = 1
while row <= 4:
    col = 1
    while col <= row:
        print(chr(ord("A")+n-row+col-1), end="")
        col += 1
    print()
    row += 1
"""

#    *
#   **
#  ***
# ****
"""
# rows = 4, columns=4,data=*s at end, same as current row number and rest all spaces to fill up 4 before
n = int(input("enter a number "))
row = 1
while row <= n:
    space = n - row
    while space:
        print(" ", end="")
        space -= 1
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print()
    row += 1
"""

# homework
# xxxx
# xxx
# xx
# x
"""
# rows=4,columns i.e. x = start by 4 and decrease for each row
n = int(input("enter a number "))
row = 1
while row <= n:
    col = n - row + 1
    while col:
        print("x", end="")
        col -= 1
    print()
    row += 1
"""

# homework
# xxxx
#  xxx
#   xx
#    x
"""
# rows = 4, spaces = 0,1,2,3, stars = 4,3,2,1
n = int(input("enter a number "))
row = 1
while row <= n:
    space = row - 1
    while space:
        print(" ", end="")
        space -= 1
    col = n - row + 1
    while col:
        print("x", end="")
        col -= 1
    print()
    row += 1
"""

# homework
# 1111
#  222
#   33
#    4
"""
# rows=4, spaces=0,1,2,3, numbers=4,3,2,1, data=rownum
n = int(input("enter a number "))
row = 1
while row <= n:
    space = row - 1
    while space:
        print(" ", end="")
        space -= 1
    col = n - row + 1
    while col:
        print(row, end="")
        col -= 1
    print()
    row += 1
"""

# homework
#    1
#   22
#  333
# 4444
"""
# rows=4,spaces=3,2,1,0, numbers=1,2,3,4, data=row num
n = int(input("enter a number "))
row = 1
while row <= n:
    space = n - row
    while space:
        print(" ", end="")
        space -= 1
    col = row
    while col:
        print(row, end="")
        col -= 1
    print()
    row += 1
"""

# homework
# 1 2 3 4
#   2 3 4
#     3 4
#       4
"""
# rows=4, spaces=0,1,2,3, nums=4,3,2,1, data = col number
n = int(input("enter a number "))
row = 1
while row <= n:
    space = row - 1
    while space:
        print(" ", end="")
        space -= 1
    col = 1
    while col <= n - row + 1:
        print(col, end="")
        col += 1
    print()
    row += 1
"""

# homework
#       1
#     2 3
#   4 5 6
# 7 8 9 10
"""
# rows=4, spaces=3,2,1,0, nums=1,2,3,4,data=start with rownum and increment
n = int(input("enter a number "))
row = 1
count = 1
while row <= n:
    space = n - row
    while space:
        print(" ", end="")
        space -= 1
    col = 1
    while col <= row:
        print(count, end="")
        count += 1
        col += 1
    print()
    row += 1
"""

#    1
#   121
#  12321
# 1234321
"""
# rows=4, spaces=3,2,1,0, nums=1,3,5,7, data=1 to rownum increment, decrement till 1
n = int(input("enter a number "))
row = 1
while row <= n:
    space = n - row
    while space:
        print(" ", end="")
        space -= 1
    col = 1
    while col <= row:
        print(col, end="")
        col += 1
    start = row - 1
    while start:
        print(start, end="")
        start -= 1
    print()
    row += 1
"""

# homework
# 1234554321
# 1234**4321
# 123****321
# 12******21
# 1********1
"""
# rows=4, cols=10, data=1to5,5to1, 1to4,4to1,2stars in between,1 to 3, 3to1, 4 stars in between, 1to2 1to 2 6 stars in between ,1 1 8 stars in between
n = int(input("enter a number "))  # 5
row = 1
while row <= n:
    col = 1
    while col <= n-row+1:
        print(col, end="")
        col += 1
    star = 2 * (row-1)
    while star:
        print("*", end="")
        star -= 1
    col = n - row + 1
    while col:
        print(col, end="")
        col -= 1
    print()
    row += 1
"""