# hello world program
"""
if __name__ == "__main__":
    print("hello world")
    print()
"""

# data types
"""
- int - 5
- string - "s"
- boolean - True
- float - 1.2
"""

# variables
"""
- letters
- underscores
- numbers - don't start with it
"""

# data types and variables program
"""
import sys
i = 8
print(i)  # 1000 in binary
print(sys.getsizeof(i) - sys.getsizeof(int())  # 4 bytes  # increase when number crosses a limit
print()

s = "s"
print(s)
print(ord(s))  # ascii value is 115  # 1100111 in binary
print(chr(115))
print(sys.getsizeof(s) - sys.getsizeof(str())  # 1 byte  # increases per character
print()

b = True
print(b)
print(sys.getsizeof(i) - sys.getsizeof(bool())  # 4 bytes
print()

f = 1.2
print(f)
print(sys.getsizeof(b) - sys.getsizeof(float())  # 4 bytes  # doesnt increase for big number as it is converted to e and leaves digits after decimal
print()
"""

# memory allocation
"""
- memory block has value and name
- binary representation of different data types like int and string is differentiated by data type
"""

# ASCII
"""
- american standard code for information interchange
- represent characters(letters,numbers,symbols) as numbers to store in memory
- english language subset of unicode
- 128 characters from unicode's 1114112 characters
- used in emails, programming, text files, data conversations
- a(97) - A(65) = 32 i.e. just flip one bit to change case
- a -->      1  1  0  0 0 0 1
- A -->      1  0  0  0 0 0 1
-        128 64 32 16 8 4 2 1
"""

# memory allocation for -ve numbers eg: -5
"""
- binary of +ve number                               00000000000000000000000000000101
- take 1's compliment i.e. exchange 0s and 1s        11111111111111111111111111111010
- take 2's compliment i.e. add 1 to 1's compliment   11111111111111111111111111111011
- negative number read from memory - eg:             11111111111111111111111111111011 - 1 in first bit means -ve
- take 1's compliment i.e. exchange 0s and 1s        00000000000000000000000000000100
- take 2's compliment i.e. add 1 to 1's compliment   00000000000000000000000000000101 - +ve value i.e. 5
- saves extra bit for 0 and -0
"""

# arithmetic operators
"""
- %
- +
- -
- *
- / (true div)
- // (floor div)
"""

# arithmetic operators program
"""
print(2/4)  # true float
print(2//4)  # floor int
print(2.0/4)  # true float
print(2.0//4)  # floor float
print()
"""

# relational operators
"""
==
>
<
>=
<=
!=
"""

# relational operators program
"""
a = 2
b = 3
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print()
"""

# assignment operators
"""
=
"""

# logical operators
"""
and
or
not
"""

# logical operators program
"""
a = 1
print(not a)
a = 0
print(not a)
"""
