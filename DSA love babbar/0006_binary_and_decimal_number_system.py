# positive decimal to binary - approach 1
"""
7
7/2 = 3  7%2 = 1
3/2 = 1  3%2 = 1
1/2 = 0  1%2 = 1

1     1     1
4  +  2  +  1
2^2  2^1  2^0

reverse consolidate 111
1
1 + 10 = 11
11 + 100 = 111
"""

# positive decimal to binary - approach 2
"""
7
7&1 1 7>>1=3
3&1 1 3>>1=1
1&1 1 1>>1=0

reverse consolidate 111
1
1 + 10 = 11
11 + 100 = 111
"""

# negative decimal to binary
"""
ignore negative sign
convert positive decimal to binary as already known
for making the binary negative - take 2's complement i.e. 1's complement + 1
"""

# positive binary to decimal
"""
keep counter
keep sum
while number does not turn 0
if bit is 1 multiply it by 2**counter and add to sum

1   0   1
8   4   2

8+2 = 10
"""

# negative binary to decimal
"""
check is first bit is 1 to identify negative binary
if so,
to convert to positive binary - take 2's complement i.e. 1's complement + 1
convert positive binary to decimal as already known
to make the decimal negative - add negative sign
"""

#########################################################################################

# positive decimal to binary program
"""
n = int(input("enter a number "))
ans = 0
i = 0
while n != 0:
    bit = n & 1
    n = n >> 1
    ans = ans + (bit * 10**i)
    i += 1
print(ans)
"""

# homework - revisit
# negative decimal to binary program
"""
def positive_decimal_to_binary(n):
    ans = 0
    i = 0
    while n != 0:
        bit = n & 1
        n = n >> 1
        ans = ans + (bit * 10**i)
        i += 1
    return ans
def count_digits_positive_bin(n):
    i = 0
    while n != 0:
        n = n // 10
        i += 1
    return i
def one_complement(n, digits_count):
    i = 0
    ans = 0
    for _ in range(32-digits_count):
        bit_complement = 1
        ans = (bit_complement * 10 ** i) + ans
        i += 1
    ans = ans * 10 ** digits_count
    print(ans)
    i = 0
    while n != 0:
        digit = n % 10
        digit_complement = 1 if digit == 0 else 0
        n = n // 10
        ans = ans + (10**i * digit_complement)
        i += 1
    return ans
def two_complement(n):
    ans = 0
    i = 0
    added = False
    while n != 0:
        digit = n % 10
        if not added:
            if digit == 0:
                digit = 1
                added = True
            else:
                digit = 0
        n = n // 10
        ans = (digit * 10 ** i) + ans
        i += 1
    return ans
if __name__ == "__main__":
    n = int(input("enter a -ve number "))
    positive_decimal = 0 - n
    positive_bin = positive_decimal_to_binary(positive_decimal)
    positive_bin_digits_count = count_digits_positive_bin(positive_bin)
    one_com = one_complement(positive_bin, positive_bin_digits_count)
    two_com = two_complement(one_com)
    print(two_com)
"""

# positive binary to decimal program
"""
n = int(input("enter a binary number "))
i = 0
ans = 0
while n != 0:
    digit = n % 10
    n = n // 10
    if digit:
        ans = ans + 2**i
    i += 1
print(ans)
"""

# homework identified by self - revisit
# negative binary to decimal program
"""
def positive_binary_to_decimal(n):
    i = 0
    ans = 0
    while n != 0:
        digit = n % 10
        n = n // 10
        if digit:
            ans = ans + 2**i
        i += 1
    return ans
def count_digits_positive_bin(n):
    i = 0
    while n != 0:
        n = n // 10
        i += 1
    return i
def one_complement(n):
    i = 0
    ans = 0
    while n != 0:
        digit = n % 10
        digit_complement = 1 if digit == 0 else 0
        n = n // 10
        ans = ans + (10**i * digit_complement)
        i += 1
    return ans
def two_complement(n):
    ans = 0
    i = 0
    added = False
    while n != 0:
        digit = n % 10
        if not added:
            if digit == 0:
                digit = 1
                added = True
            else:
                digit = 0
        n = n // 10
        ans = (digit * 10 ** i) + ans
        i += 1
    return ans
if __name__ == "__main__":
    n = int(input("enter a -ve binary number "))  # 11111111111111111111111111111010
    one_com = one_complement(n)
    two_com = two_complement(one_com)
    positive_decimal = positive_binary_to_decimal(two_com)
    negative_decimal = 0 - positive_decimal
    print(negative_decimal)
"""
