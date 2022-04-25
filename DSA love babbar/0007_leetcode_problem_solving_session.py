# problem programs
# https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2**31
        int_max = 2**31 - 1
        n = x
        if x < 0:
            x = 0 - x
        ans = 0
        while x != 0:
            digit = x % 10
            if ans > int_max / 10 or ans < int_min / 10:
                return 0
            ans = (ans*10) + digit
            x = x // 10
        if n < 0:
            ans = 0 - ans
        return ans
"""

# complement of integer - logic
"""
original: 5
binary of original:                                         00000000000000000000000000000101

binary mask of original number:                               
(right shift till number becomes 0)                         00000000000000000000000000000000
(left shift and or with 1 that many times)                  00000000000000000000000000000111

not of original: ~5
binary of not of original:                                  11111111111111111111111111111010

and the binary not with the mask:                           00000000000000000000000000000010

convert to decimal: 2
"""

# problem programs
# https://leetcode.com/problems/complement-of-base-10-integer/
"""
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # edge case
        if n == 0:
            return 1
        m = n
        mask = 0
        while m != 0:
            mask = mask << 1
            mask = mask | 1
            m = m >> 1
        ans = ~n & mask
        return ans
"""

# https://leetcode.com/problems/power-of-two/
# not optimized approach
# another approach - homework - revisit
# optimized approach
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            if ans < 2147483647:
                ans = ans * 2
        return False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n != 1:
            remainder = n % 2
            if remainder != 0:
                return False
            n = n // 2
        return True

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        set_bits = 0
        while n != 0:
            if n & 1 == 1:
                if set_bits == 1:
                    return False
                else:
                    set_bits += 1
            n = n >> 1
        if set_bits == 1:
            return True
        return False
"""
