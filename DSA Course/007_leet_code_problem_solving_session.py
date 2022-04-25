# todo: program: other solutions
# program: https://leetcode.com/problems/reverse-integer/
# positive or negative 32 bit integer
# if reversing causes it to go out of range i.e. -2^31 to 2^31 - 1, return 0
# we shouldn't even store bigger integer in memory
# logic: int range: -2147483647 to 2147483646
# logic: take digit y mod 10, take new number by div 10, save reverse by multiplying 10 each time
# logic: to not exceed range, instead of checking if rev*10 + digit > max, check: rev > (max-digit)/10 for +ve and check: rev > (max-digit)/10 + 0.1 for negative
"""
def reverse(n):
    negative = True if n < 0 else False
    if negative:
        n = abs(n)
    rev = 0
    seq = 0
    max = 2147483646
    while n != 0:
        digit = n % 10
        if negative:
            if rev > ((max - digit) / 10) + 0.1:
                print(rev)
                print(((max - digit) / 10) + 0.1)
                return 0
        else:
            if rev > (max - digit)/10:
                return 0
        rev = (rev * 10) + digit
        n = n // 10
        seq += 1
    if negative:
        rev = 0 - rev
    return rev
num = int(input("enter num "))
print(reverse(num))
"""

# program: mask creation
# logic: right shift until n != 0 to get all real bits, make mask as 0 and left shift and or with 1 each time to add 1, return 1 for 0

# todo: program: other solutions
# program: https://leetcode.com/problems/complement-of-base-10-integer/
# program: https://leetcode.com/problems/number-complement/
# eg: 5 -> 101 -> 010 -> 2 (no preceding 1s)
# logic: after complement(~), use mask all 0s and last necessary(3) bits 1 so that everything becomes 0 and last part is as is when ~ and mask is &
# logic: always handle edge cases also
"""
def real_complement(n):
    b = bin(n)[2:]
    b = list("0"*(32-len(b)) + b)
    for i in range(len(b)):
        b[i] = '0' if b[i] == '1' else '1'
    b = "".join(b)
    return int(b,2)
def complement(num):
    n = num
    mask = 0
    if n == 0:
        return 1
    while n != 0:
        n = n >> 1
        mask = (mask << 1) | 1
    return real_complement(num) & mask
print(complement(6))
"""

# todo: program: other solutions
# program: https://leetcode.com/problems/power-of-two/
# whether number can be described in power of two or not
# my logic: keep dividing by 2 and if remainder is odd, false
# logic: get powers of 2 from 0 to 30 i.e. int range (exclude 31 as i.e. -1) and compare with given num
# logic: negative ans is not possible
# logic: brute force not optimized
# logic: do not calculate pow each time, multiply 2 to prev ans
# logic: do not multiple 2 in last iteration as that will go out of range hence check if > range
# logic: divide by 2 from both sides for checking range so that comparison itself doesnt break
"""
def power_of_two(num):
    comp = 1
    for i in range(0, 31):
        if 2**i == num:
            return True
        if comp < (2**31 - 1)/2:
            comp = comp * 2
    return False
print(power_of_two(16))
"""
