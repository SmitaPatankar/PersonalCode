# contest: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-3?utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_contest3

# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-3/problems/14474 - raksha bandhan
# ninja celebrating rakshabandhan with n sisters
# each sister wants to tie him one rakhi with some number
# array with all rakhi numbers
# sum of tied rakhis should be positive (not 0 or neg)
# count max no of rakhis he can have
# eg: [ 1, -1, 0 ]
# ans: 2 i.e. 0 and 1
# upto 10^4 rakhis or sisters
# -10^9 to 10^9 rakhi number
# 1 sec
# that means max n^2 complexity
# 3 -3 --> 1 i.e. 3
# 1 -2 2 --> 3 i.e. 1+2-2 i.e. 1
# my logic sort desc and keep taking until value becomes 0 or lesser
"""
def raksha_bandhan(arr):
    arr.sort(reverse=True)
    count = 0
    sum = 0
    for element in arr:
        if sum + element > 0:
           count += 1
           sum += element
        else:
            break
    return count
print(raksha_bandhan([3,-1,2]))
"""

# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-3/problems/16650?leftPanelTab=0 - catch fish
# pond with fishes divided in n segments
# each segment can have max 1 fish
# we want to catch k fish in 1 attempt
# drop net any size <= pond on a continuous segment
# minimize size of net
# my logic: minimum max size of net
# eg:
# 5 segments
# [1,0,1,0,1]
# catch 2 fish
# ans: 1,0,1 or other 1,0,1 i.e. size=3
# pond may not contain k fishes
# 2 to 10^5 fishes needed or have
# 1 sec
# from each point collect k and return min of those sizes - brute force
# similar using 2 pointer
"""
def minimum_net(n, k, fish):
    ans = -1
    i = 0
    j = 0
    sum = 0
    while i < n and j < n:
        print(f"{i} {j}")
        sum += fish[j]
        if sum >= k:
            temp_ans = j - i + 1
            sum = 0
            i += 1
            j = i
            if temp_ans == k:
                return temp_ans
            ans = temp_ans if ans == -1 else min(ans, temp_ans)
        else:
            j += 1
    return ans
print(minimum_net(5, 1, [1,0,1,1,0]))
"""

# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-3/problems/14865?leftPanelTab=0 - ninja technique
# place copies of ninja at some points such that he appears to be everywhere
# there are n segments on x axis
# endpoints are stored in 2d array
# place copy anywhere on x
# all segments containing this point should show ninja everywhere on the corresponding segments
# least no. of copies to cover each statement
# eg:
# n = 2 segments
# endpoints = A = [ ( 0 , 2 ) , ( 2 , 5 ) ]
# ans: just need to place one copy at 2
# logic:
# sort by ending coordinate of each array
# check if last places value covers this one, else place at its last
"""
class Segment:
    def __init__(self,start, end):
        self.start = start
        self.end = end
def ninja_technique(n, a):
    last_place = None
    ans = None
    for i in range(len(a)):
        a[i] = Segment(a[i][1],a[i][0]) if a[i][0] > a[i][1] else Segment(a[i][0],a[i][1])
    a.sort(key=lambda element: element.end)
    for segment in a:
        if not last_place or segment.start > last_place:
            last_place = segment.end
            ans = ans + 1 if ans else 1
    return ans if ans else -1
print(ninja_technique(2, [(1,-13),(-11,2),(-7,18),(-14,9),(-3,16)]))  # 1
"""

# contest: program: https://www.codingninjas.com/codestudio/contests/love-babbar-contest-3/problems/16572?leftPanelTab=0 - make it equal
# 3 integers a,b and c
# in one move we can flip one bit in a or b
# return minimum moves to make a &AND b = c
# eg: 2,3, & 5
# i.e. 010 011 101
# 010 --> 011 --> 111 --> 111 --> 101
# 011 --> 011 --> 011 --> 111 --> 111
# ans = 4
"""
def flip(a, b, c, ans=0):
    if a == 0 and b == 0 and c == 0:
        return ans
    last_bit_a = a & 1
    last_bit_b = b & 1
    last_bit_c = c & 1
    if last_bit_c == 1:
        if last_bit_a == 0:
            ans += 1
        if last_bit_b == 0:
            ans += 1
    else:
        if last_bit_a == 1 and last_bit_b == 1:
            ans += 1
    a = a >> 1
    b = b >> 1
    c = c >> 1
    return flip(a, b, c,ans)
print(flip(2,3,5))  # 4
"""
