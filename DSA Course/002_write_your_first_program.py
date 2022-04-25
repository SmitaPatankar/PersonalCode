# todo: python: namespaces

# todo: python: data types memory usage including negative numbers
# data types details
"""
different types take different memory - depends on compiler - data is stored in binary form in these bytes(bits)

- int (4 bytes in cpp)
- float (4 bytes in cpp)
- bool (1 byte in cpp)
"""

# variable naming convention
"""
- letters, numbers, underscores
- do not start with number
"""

# program: data type, variable
"""
a = 123
print(a)
print(a.__sizeof__())  # 28
b = True
print(b)
print(b.__sizeof__())  # 28
c = 1.2
print(c)
print(c.__sizeof__())  # 24
"""

# TODO: computers: ascii table
# TODO: math: how two's complement done twice returns the original number
# TODO: computers: how 0 is given one representation in positive and not in negative i.e. negative range is 2^31 and positive is 2^31-1
# how is data stored in memory
"""
integer
########
8
4 bytes = 32 bits
....................................0   0   0   0   1   0   0   0
--------    --------    --------    -   -   -   -   -   -   -   -
....................................128 64  32  16  8   4   2   1   

5
1   0   1
4   2   1

letter
######
a - done using ASCII table as it maps characters to numbers - 97
1 byte = 8 bits
0   1   1   0   0   0   0   1
128 64  32  16  8   4   2   1

negative number
###############
first bit is 0 for positive and 1 for negative
-5
- ignore negative sign - 5
- convert to binary - 00000000000000000000000000000101
- take 1's complement i.e. exchange 0s and 1s - 11111111111111111111111111111010
- take 2's complement i.e. add 1 to above - 11111111111111111111111111111011
- all this is done instead of using last bit as sign bcoz:
    - it wud represent 0 as +0 and -0 in two ways
    - it wud also reduce the range from (- 2^31 : 2^31 - 1) to (- 2^31 -1 : 2^31 - 1)

back from binary to negative number
###################################
- 11111111111111111111111111111011 - first bit represents negative i.e. 1
- take 1's complement - 0000000000000000000000000000100
- take 2's complement - 0000000000000000000000000000101
- -5

data types are used because we cant recognize which data type to convert the binary into i.e. letters, numbers etc
"""

# program: letter to number and back
"""
c = "a"
print(ord(c))  # 97
print(chr(97))  # a
"""

# operators list
"""
module - %
arithmetic - + - * /
relational - == >= <= != < >
assignment - =
logical - and or not
"""

# TODO: computers: check if o/p is stored in memory block when we directly print it without saving in variable
# program: arithmetic operator
"""
print(3 / 5)  # 0.4  # true div  # if any one number is float, this will be float even if there is .0 at end
print(2 // 5)  # 0  # floor div  # if any one number is float, this will also be float bur floored one
"""

# program: relational operator
"""
a = 1
b = 2
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
"""

# program: logical operator
"""
a = 5
print(not a)  # False
"""
