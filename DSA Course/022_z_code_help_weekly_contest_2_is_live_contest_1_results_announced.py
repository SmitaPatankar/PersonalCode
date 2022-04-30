# https://www.codingninjas.com/codestudio/contests/love-babbar-contest-ii?utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_contest2

# program: contest: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-ii/problems/14818
# test was attended by N students
# marks of each student are in array
# person got rank K but forgot marks
# find the marks
# ranks start from 1
# duplicate marks also have unique ranks
# eg: [ 2, 5, 4, 4, 5 ]  # rank 3 # ans 4
"""
def class_test(n,a,k):
	a.sort(reverse=True)
	return a[k-1]
print(class_test(10,[12,10,2,3,9,6,5,8,1,1], 2))
"""

# program: contest: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-ii/problems/15566?leftPanelTab=0
# bob is buying binary string of size N
# shop gave him an integer P, binary string S and told cost
# Cost =  S[0] * (P^0) + S[1] * (P^1) + S[2] * (P^2) … S[N - 1] * (P^(n-1))
# perform 2 operations on string to make cost as low as possible
# can flip bit of any index
# can select same index both times
# find minimum cost
# print string at end
# eg:
# N=5 P=3
# 01101
# 0 * (3^0) + 1 * (3^1) + 0 * (3^2) + 0 * (3^3)  + 0 * (3^4)
# ans: 01000
# logic:
# righter bits are multiplied to higher powers of p i.e. cost increases when righter bits are 1
# try to make them 0
# cases:
# 0110111 --> 2 or more 1s --> flip last 2
# 0000000 --> no 1s --> flip any twice
# 0000100 --> exactly one 1 --> flip it to 0 and flip 0th to 1
"""
def binary_shopping(s, p):
    s = list(s)
    one_indexes = []
    for i in range(len(s)-1,-1,-1):
        if s[i] == "1":
            one_indexes.append(i)
        if len(one_indexes) == 2:
            break
    if len(one_indexes) == 2:
        s[one_indexes[0]] = "0"
        s[one_indexes[1]] = "0"
    elif len(one_indexes) == 1:
        s[one_indexes[0]] = "0"
        s[0] = "1"
    else:
        s[0] = "1"
        s[0] = "0"
    s = "".join(s)
    return s
print(binary_shopping("0000000 ", 4))
"""

# program: contest: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-ii/problems/14871
# given an array arr
# given Q queries
# query is X such that we have to find
# Find the largest index IND such that ARR[1] & ARR[2] & …...ARR[IND] >=X
# eg:
# arr = [3,7,9,16]
# q = 2
# query 1 = 2 --> 3 & 7 = 011 & 111 i.e. 011 i.e. 3 >=2 , 3 & 7 & 9 i.e. 011 & 1001 i.e. 1001 i.e. 9 not greater so ans is 1 + 1 starting from 1 i.e. 2
# query 2 = 3....
# logic:
# eg: [3,7,9,1,6] ans: [2,3]
# create array with all ands
# eg: [3, &7, &9, &1, &16]
# for each query, perform binary search
"""
def bitwise_and(n, q, arr, queries):
    ands = []
    answers = []
    ands.append(arr[0])
    for i in range(1, len(arr)):
        ands.append(arr[i] & ands[-1])
    for query in queries:
        start = 0
        end = len(ands) - 1
        ans = 0
        while start <= end:
            mid = start + ((end-start)//2)
            if ands[mid] >= query:
                ans = mid + 1  # indexing starts from 0 for ans
                start = mid + 1
            else:
                end = mid - 1
        answers.append(ans)
    return answers
print(bitwise_and(4, 2, [3,7,9,16],[2,1]))
"""

# program: contest: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-ii/problems/14751
# street of length n
# light up the street with lights
# there are m streetlights
# ith streetlight can be installed at Ci position
# range of streetlights is given such that Ci will enlighten ci-R to ci+R
# find minimum lights required
# -1 for no ans
# eg:
# N=10, M=3
# C = [2,4,7] ( The positions of the streetlights )
# R = 3 ( The range of the street-lights)
# ans = 2 & 7 i.e. 2
# positioning of bulbs starts from 1
# TODO: revise
"""
def light_up_street(l, r, checkpoints):
    ans = 0
    lit_range = 0
    possible_to_light = 0
    for checkpoint in checkpoints:
        # if previous area is not lit
        if checkpoint - r - 1 > lit_range:
            # if previous area is impossible to light because of lack of bulb covering that area
            if checkpoint - r - 1 > possible_to_light:
                return -1
            # possible to light previous area by turning on previous bulb
            else:
                ans += 1
                lit_range = possible_to_light
        # previous area is lit
        else:
            pass
        possible_to_light = checkpoint + r
    # if entire street is not lit
    if lit_range < l:
        # if last bulb doesnt suffice
        if possible_to_light < l:
            return -1
        # last bulb suffices
        else:
            ans += 1
    return ans
print(light_up_street(10,3,[2,4,7]))
"""