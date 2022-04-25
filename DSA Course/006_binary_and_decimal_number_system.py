# decimal details
"""
15    -->                         1   5
-----------------------------------------
system -->            1000    100 10  1
"""

# binary details
"""
10     -->          1   0   1   0
----------------------------------
system -->  32  16  8   4   2   1
"""

# program: reverse number - logic: n = 0, ans = 0, ans = (digit * 10^n) + ans, n++

# todo: math: how decimal to binary works by dividing by 2 and consolidating remainders and reversing them
# program: decimal to binary
# logic: divide num by 2 and store remainders and join, new num is quotient of previous division - will have to reverse at end - wait when num becomes 0
# another logic: & with 1 and right shift until number becomes 0 to find each bit and then reverse the ans
"""
n = 5
ans = 0
seq = 0
while n != 0:
    bit = n & 1
    n = n >> 1
    ans = (bit * 10**seq) + ans
    seq += 1
print(ans)
"""

# todo: math: how divide by 2 works each time for dec to bin
# hw: program: negative decimal to binary: logic: binary, 2's complement
"""
def negative_decimal_to_binary(nd):
    print(f"nd is {nd}")  # -6
    d = positive(nd)
    print(f"d is {d}")  # 6
    b = binary(d)
    print(f"b is {''.join(b)}")  # 00000000000000000000000000000110
    o = one_complement(b)
    print(f"o is {''.join(o)}")  # 11111111111111111111111111111001
    t = two_complement(o)
    print(f"t is {''.join(t)}")  # 11111111111111111111111111111010
    return "".join(t)
def positive(nd):
    return 0 - nd
def binary(d):
    b = []
    while d:
        b.append(str(d % 2))
        d = d // 2
    while len(b) != 32:
        b.append("0")
    b.reverse()
    return b
def one_complement(b):
    ans = []
    for value in b:
        if value == "0":
            ans.append("1")
        else:
            ans.append("0")
    return ans
def two_complement(o):
    for i in range(len(o)-1, -1, -1):
        if o[i] == '0':
            o[i] = '1'
            break
        else:
            o[i] = '0'
    return o
nd = -6
b = negative_decimal_to_binary(nd)
"""

# program: binary to decimal
# logic: multiply each bit by its value like 2,4,8 etc and add
# logic: decimal eg: 6 can either be read as decimal or shifted, done and on as binary
# logic: binary, eg: 110 can be used by taking each digit by % and new num by // itself, it cannot be used for bit operations as computer would again convert it to binary i.e. big and wrong
"""
n = 110
seq = 0
ans = 0
while n != 0:
    digit = n % 10
    if digit == 1:
        ans = ans + (digit * 2**seq)
    n = n // 10
    seq += 1
print(ans)
"""
