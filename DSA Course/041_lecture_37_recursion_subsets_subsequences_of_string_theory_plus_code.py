# todo: tbd: hw: complexity of recursion subsets
# program: https://leetcode.com/problems/subsets/
# integer array given - [1,2,3]
# return power set i.e. set of all subsets
# collect ans
# for each index
# make 2 calls one by adding that element and one by not adding
# like that when index exceeds return
# but before returning append o/p to main ans for collecting all last levels
# power set of n elements is 2^n length
"""
def solve(nums, current_ans, total_as, i):
    if i >= len(nums):
        total_as.append(current_ans)
        return
    # exclude
    solve(nums, current_ans, total_as, i+1)
    # include
    solve(nums, current_ans+[nums[i]], total_as, i+1)
def subsets(nums):
    total_ans = []
    current_ans = []
    i = 0
    solve(nums, current_ans, total_ans, i)
    return total_ans
print(subsets([1,2,3]))
"""

# program: https://www.codingninjas.com/codestudio/problems/subsequences-of-string_985087
# string given
# return all non empty possible subsequences
# delete 0 or more letters and keep sequence same
# eg: str --> str s t r st tr sr
"""
def solve(s, output, ans, i):
    if i >= len(s):
        if output != "":
            ans.append(output)
        return
    solve(s,output,ans,i+1)
    solve(s,output+s[i],ans,i+1)
def subsequences(str):
    output = ""
    ans = []
    i = 0
    solve(str, output, ans, i)
    return ans
print(subsequences("str"))
"""

# bit manipulation
"""
1 << n = 2^9
eg:  1 2 4 8 16
i.e. 2^0 2^1 2^2.....

to check whether ith bit of x is 1 or not, we can do x & (1 << i)
eg: ...1000 & (1000) = non zero --> set
eg: ...0000 & (1000) = zero --> not set

n elements have 2^n subsets
eg: blank --> {}
eg: 1 --> {},{1}
eg: 12 --> {}{1}{2}{12}
for every number we can include or exclude it and so on - multiply all options i.e. 2^n

if we write first n binary numbers i.e 0 to n-1, we can just consider bits as include exclude that digit
eg: 010 would mean {2} excluding 1 and 3

bit masking questions have small n

complexity of subsets using bit masking is O(2^n * n) --> 2^n is no of outputs & n is no of bits in each output
"""

# hw: program: find subsets of {1,2,3} via bits - https://leetcode.com/problems/subsets/
"""
def subsets(nums):
    ans = []
    count = 1<<len(nums)
    print(f"no of subsets is {count}\n")
    for i in range(count):
        print(f"calculating set for {i}")
        subset = []
        for j in range(len(nums)):
            print(f"checking bit at {j}")
            bit_mask = 1 << j
            print(f"bit mask is {bit_mask}")
            if i & bit_mask != 0:
                print(f"bit is set - adding {nums[j]} to currently building subset")
                subset.append(nums[j])
            else:
                print(f"bit is not set - not adding element at {j} i.e. {nums[j]} to currently building subset")
            print()
        ans.append(subset)
        print(f"adding complete subset {subset} to ans")
    return ans
print(subsets([1,2,3]))
"""

# hw: program: find subsequences of "str" via bits - https://www.codingninjas.com/codestudio/problems/subsequences-of-string_985087
"""
def subsequences(str):
    ans = []
    count = 1<<len(str)
    print(f"no of subsets is {count}\n")
    for i in range(count):
        print(f"calculating set for {i}")
        subsequence = ""
        for j in range(len(str)):
            print(f"checking bit at {j}")
            bit_mask = 1 << j
            print(f"bit mask is {bit_mask}")
            if i & bit_mask != 0:
                print(f"bit is set - adding character at {j} i.e. {str[j]} to currently building subsequence")
                subsequence += str[j]
            else:
                print(f"bit is not set - not adding character at {j} i.e. {str[j]} to currently building subsequence")
            print()
        if subsequence:
            ans.append(subsequence)
        print(f"adding complete subsequence {subsequence} to ans")
    return ans
print(subsequences("str"))
"""

# todo: subsets without duplicate elements
# can change from list to set and back

# todo: array of nums - find subsequence such that xor is maximum
# use get subsets logic from above and when xor is maximum than current stored xor, replace and return at end
