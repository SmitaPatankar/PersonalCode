# bitwise operators details
"""
and - & - 00 = 0, 10 = 0, 01 = 0, 11 = 1 - both bits should be 1 for 1
4-->    1   0   0
        &   &   &
6 -->   1   1   0
------------------
4 -->   1   0   0

###########################################################################

or - | - 00 = 0, 10=1, 01=1,11=1 - any one it should be 1 for 1

4 -->   1   0   0
        |   |   |
6 -->   1   1   0
------------------
6 -->   1   1   0

###########################################################################

not - ~ - 0 to 1, 1 to 0

4 -->   00000000000000000000000000000100
~
-----------------------------------------------------------------------
?  =    11111111111111111111111111111011 (negative as first bit is 1)
?  =    00000000000000000000000000000100 -> 1st complement for printing
-5 =    00000000000000000000000000000101 -> 2's complement for printing

###########################################################################

xor - ^ -  00=0,01=1,10=1,11=0 - don't have both 1 and 0 is 0

4 -->   1   0   0
^
6 -->   1   1   0
--------------------
2 -->   0   1   0
"""

# program: bitwise operators
"""
a = 4
b = 6
print(f"a is {a}")
print(f"b is {b}")
print(f"a&b is {a&b}")
print(f"a|b is {a|b}")
print(f"~a is {~a}")
print(f"a^b is {a^b}")
"""

# left and right shift operators details
"""
left shift

5 << 1
5  --> 00000000000000000000000000000101
10 --> 00000000000000000000000000001010

3 << 2
3  -->  00000000000000000000000000000011
12 -->  00000000000000000000000000001100

mostly gets multiplied by 2 - not always - not for big numbers like 01xxxxxxx bcoz it becomes 10xxxx i.e. negative

###########################################################################

right shift

15 >> 1

15  --> 00000000000000000000000000001111
7   --> 00000000000000000000000000000111

5 >> 2

5   --> 00000000000000000000000000000101
1   --> 00000000000000000000000000000001

mostly divides by 2

###########################################################################

pad +ve with 0
compiler dependent padding for -ve
"""

# program: left shift right shift
"""
print(17>>1)  # 8
print(17>>2)  # 4
print(19<<1)  # 38
print(19<<2)  # 76
"""

# program: increment (same for decrement) - utility
"""
i = 1
i+=1
print(i)
"""

# program: for loop
"""
n = int(input("enter n "))
for i in range(1, n+1):
    print(i)
"""

# program: for loop - break
"""
n = int(input("enter n "))
for i in range(1, n+1):
    if i <= 5:
        print(i)
    else:
        break
"""

# program: sum from 1 to n
"""
n = int(input("enter n "))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)
"""

# program: fibonacci series - logic: current num is sum of previous 2 nums
"""
n = 10
a = 0
print(a,end=" ")
b = 1
print(b,end=" ")
for i in range(n-2):
    c = a + b
    print(c,end=" ")
    a = b
    b = c
"""

# program: prime number
"""
n = int(input("enter n "))
is_prime = True
for i in range(2,n):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)
"""

# program: continue - skip interation
"""
for i in range(6):
    if i == 3:
        continue
    print(i)
"""

# todo: python: scope of variable
# variables and scopes

# todo: python: operator precedence
# operator precedence
"""
use brackets to not memorize it
"""

# program: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/ - logic: to get digit % by 10, to get remaining number, / by 10
"""
n = 12345
sum = 0
product = 1
while n != 0:
    digit = n % 10  # 5 4   3   2   1
    sum = sum + digit
    product = product * digit
    n = n // 10  # 1234 123 12  1   0
print(f"sum is {sum}")
print(f"product is {product}")
print(f"difference between product and sum is: {product - sum}")
"""

# program: https://leetcode.com/problems/number-of-1-bits/ - logic: check right bit and right shift until number becomes 0 - logic: to check last do and with 1 as every other bit will become 0 by & with 0, and only last bit will become 1 if it was 1 else 0 by & with 1
"""
n = 3
count = 0
while n != 0:
    if n & 1 == 1:
        count += 1
    n = n >> 1
print(f"count is {count}")
"""
