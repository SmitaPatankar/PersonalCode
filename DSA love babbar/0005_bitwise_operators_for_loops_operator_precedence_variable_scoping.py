# bitwise operators
"""
operators:
- and - &
- or - |
- not - ~
- xor - ^
- left shift - <<
- right shift - >>

bits and their operations:
x   y   operation  o/p
0   0       &       0
0   1       &       0
1   0       &       0
1   1       &       1
0   0       |       0
0   1       |       1
1   0       |       1
1   1       |       1
0   0       ^       0
0   1       ^       1 (if any one 1 then o/p is 1)
1   0       ^       1
1   1       ^       0

x   operation   o/p
0   &           1
1   |           0

examples:
a = 2  i.e. 10
b = 3  i.e. 11
a&b     =   10 i.e. 2
a|b     =   11 i.e. 3
a^b     =   01 i.e. 1

a=2 i.e. 10 i.e. 00000000000000000000000000000010
~a          =    11111111111111111111111111111101 (i.e. -ve number after taking 2's complement)
            -->  00000000000000000000000000000010 (1's complement)
            -->  00000000000000000000000000000011 (2's complement) = -3

5 << 1 i.e. 0101 --> 1010 i.e. 10
3 << 2 i.e. 0011 --> 1100 i.e. 12
<< almost like *2 (big number will almost turn -ve if second last bit moves to last and is 1)
padding with 0 for +ve and compiler dependent for -ve

5 >> 1 i.e 0101 --> 0001 i.e. 1
>> almost like /2
padding with 0 for +ve and compiler dependent for -ve
"""

# bitwise operators program
"""
a = 2
b = 3
print(f"a & b is {a&b}")
print(f"a | b is {a|b}")
print(f"a ^ b is {a^b}")
print(f"~a is {~a}")
print(f"17 >> 1 is {17 >> 1}")
print(f"17 >> 2 is {17 >> 2}")
print(f"17 << 1 is {17 << 1}")
print(f"17 << 1 is {17 << 2}")
"""

# for loop programs
# print numbers from 1 to n - break at 5
"""
# print
n = int(input("enter the value of n "))
print("printing count from 1 to n")
for i in range(1, n+1):
    if i <= 5:
        print(i)
    else:
        break
"""

# sum of numbers from 1 to n
"""
# sum
n = int(input("enter the value of n "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
"""

# fibonacci series
"""
n = 10
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(8):
    next_num = a + b
    print(next_num, end=" ")
    a = b
    b = next_num
"""

# number is prime or not
"""
n = int(input("enter the value of n "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print("prime")
else:
    print("not prime")
"""

# for loop program with continue
"""
for i in range(1,5):
    print("hi")
    print("hey")
    continue
    print("pls reply")
"""

# variable scope program
"""
# LEGB - local, enclosed, global, builtin
print("inside module---------->")
a = "global a"
b = "global b"
c = "global c"
print(a)
print(b)
print(c)
def func1():
    print("inside func1---------->")
    a = "local a to func1"
    b = "local b to func1"
    print(a)
    print(b)
    print(c)
    def func2():
        print("inside func2---------->")
        a = "local a to func2"
        print(a)
        print("enclosed b", end=" - ")
        print(b)
        print(c)
    func2()
func1()
print("inside builtin---------->")
print(print)
"""

# variable scope program - use variable from outer scope
"""
# to modify variable from outer scope, use nonlocal(enclosed) / global keyword
a = "global a"
b = "global b"
c = "global c"
def func1():
    a = "local a to func1"
    b = "local b to func1"
    global c
    c = "global c modified by func1"
    def func2():
        print("inside func2---------->")
        a = "local a to func2"
        print(a)
        nonlocal b
        b = "local b for func1 modified by func2"
        print(b)
        global c
        c = "global c modified by func2"
        print(c)
    func2()
    print("inside func1---------->")
    print(a)
    print(b)
    print(c)
func1()
print("inside module---------->")
print(a)
print(b)
print(c)
"""

# operator precedence
"""
- https://docs.python.org/3/reference/expressions.html#operator-precedence
- use brackets instead of memorizing preference
"""

# problem programs
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1
        while n != 0:
            digit = n % 10
            n = n // 10
            sum = sum + digit
            prod = prod * digit
        return prod - sum
print(Solution().subtractProductAndSum(1234))
"""

# https://leetcode.com/problems/number-of-1-bits/
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count
print(Solution().hammingWeight(6))
"""

# pending - missed - revisit
# square root of integer as integer
"""
n = 17
for i in range(1, n-1):
    if i*i == n:
        print(i)
        break
"""