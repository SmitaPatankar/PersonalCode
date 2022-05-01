# program: swap alternate numbers in an array - logic: in for loop, check if i+1 is within array indexes if yes then swap, increment by 2 in for loop i.e. i+1 should be < size
# logic: works for odd length also, as last element is ignored if there is nothing after it
"""
def swap_alternate(a):
    for i in range(0,len(a),2):
        if i+1 < len(a):
            a[i], a[i+1] = a[i+1], a[i]
a = []
swap_alternate(a)
print(a)
a = [1]
swap_alternate(a)
print(a)
a = [1,2]
swap_alternate(a)
print(a)
a = [1,2,3]
swap_alternate(a)
print(a)
a = [1,2,3,4]
swap_alternate(a)
print(a)
"""

# todo: python internal logic: swap
# program: swap numbers - logic: use extra temporary variable
"""
a = 1
b = 2
c = a
a = b
b = c
print(a)
print(b)
"""

# todo: math: xor
# program: https://www.codingninjas.com/codestudio/problems/find-unique_625159
# array with size n, n = 2m + 1 i.e. odd, m numbers are twice and 1 number is once
# eg: if array size is 7, 3 elements are twice and one element is once
# find the unique number
# logic: if an element is xored with itself, it gives 0, 0 with another element gives that element
# logic: xor all elements together so that dupe ones get cancelled to 0 and 0 and unique one will give unique
"""
a = [1,2,3,2,1]
ans = 0
for i in range(len(a)):
    ans = ans ^ a[i]
print(ans)
"""

# todo: program: other solutions
# hw: program: https://leetcode.com/problems/unique-number-of-occurrences/
# if count of each number in array is unique, eg: 1 three, 2 ones, 3 fours - return True, else False
# logic: traverse array and keep incrementing count of element in dictionary, traverse dictionary and check if all values are unique
# another logic: use collections counter and check if length of set of values i.e. unique counts is equal to length of values i.e. counts
"""
from collections import Counter
def unique_occurences(a):
    d = Counter(a)
    return len(d.values()) == len(set(d.values()))
print(unique_occurences([1,2]))
print(unique_occurences([1,2,2]))
"""

# todo: math: vector
# tbd: vector - like dynamic array
# program: https://www.codingninjas.com/codestudio/problems/duplicate-in-array_893397
# array size is n
# numbers between 1 and n-1 are present atleast once
# eg: array of length 5 --> elements 1 to 4 are present atleast once and one of them is repeat in the empty slot
# logic: save count in dictionary and return where count is 2
# logic: xor all elements from array with all elements known to us, then we'll get element from empty slot
# eg: 1   2   3   4 ^ 1   2   3   4   5 = 5
# run in 1sec
"""
def dupe(a):
    ans = 0
    for i in range(len(a)):
        ans = ans ^ a[i]
    for i in range(1, len(a)-1):
        ans = ans ^ a[i]
    return ans
a = [1,2,3,4,4,5]
print(dupe(a))
"""

# todo: program: other solutions
# hw: program: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# array of length n
# each integer is in range 1 to n and appears once or twice
# return array of elements that appear twice
# should run in O(n)
# should use constant extra space
# eg: [2,2,3,4,4]
# logic: for each element, mark the value on corresponding index -1 as negative once and save it in result next as it would have appeared twice
# logic: while using values for counting, use abs value
# logic: we are using index as keys and - to indicate visited elements
"""
a = [2, 2, 3, 4, 4]
res = []
for element in a:
    if a[abs(element) - 1] < 0:
        res.append(abs(element))
    else:
        a[abs(element) - 1] *= -1
print(res)
"""

# todo: program: other solutions
# program: https://www.codingninjas.com/codestudio/problems/intersection-of-2-arrays
# logic: 2 pointer approach
# 2 sorted arrays of size n and m, give intersection
# [1,2,2,2,3,4]
# [2,2,3,3]
# -1 if no match
# duplicate elements are also present
# map one to one
# logic: start from first element of first array, check in second, if less, move first forward, if equal save and move both forward else move second forward
# logic: stop when any one array gets over that is pointer is not < size
# logic: 2 pointer approach
# run in 1sec
"""
a = [1,2,2,2,3,4]
b = [2,2,3,3]
i = 0
j = 0
res = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        i += 1
    elif a[i] == b[j]:
        res.append(a[i])
        i += 1
        j += 1
    else:
        j += 1
print(res)
"""

# program: https://www.codingninjas.com/codestudio/problems/pair-sum_697295
# given array
# given number
# find pairs with sum as number
# ans pairs should have sorted elements
# pairs in asc as per first
# 2 loops - one from start to end, second from element after that till end
# save pairs as min, max
# sort array of pairs
"""
a = [5,4,10,9,1,2,3,6,7,8]
s = 10
res = []
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == s:
            res.append([min([a[i],a[j]]),max([a[i],a[j]])])
res.sort()
for pair in res:
    print(f"{pair[0]} {pair[1]}")
"""

# todo: program: other solutions
# hw: program: https://www.codingninjas.com/codestudio/problems/triplets-with-given-sum_893028
# 3 loops first from 0 to last, further to last and further further to last
"""
a = [5,4,10,9,1,2,3,6,7,8]
s = 10
res = []
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i] + a[j] + a[k] == s:
                res.append([a[i],a[j],a[k]])
for triplet in res:
    print(f"{triplet[0]} {triplet[1]} {triplet[2]}")
"""

# program: sorts 0s and 1s in array
# logic: start=0, end=last
# logic: move start forward till 0, move end backwards till 1, swap and move both if opp, continue till they cross or go out of size
# logic: stop on left < right
"""
a = [0,1,1,0,0,1]
left = 0
right = len(a) - 1
while left < right:
    while a[left] == 0 and left < right:
        left += 1
    while a[right] == 1 and left < right:
        right -= 1
    if left < right:
        a[left], a[right] = a[right], a[left]
        right -= 1
print(a)
"""

# todo: program: revise
# hw: program: https://www.codingninjas.com/codestudio/problems/sort-0-1-2_631055
# logic: below
# keep 3 pointers - low, mid, high
# keep low at start for placing found 0
# keep high at end for placing found 2
# keep mid at start to traverse over each element and determine its correct position i.e. low/mid(there itself) or high
# keep moving mid to right place as below
# if mid element is 0, swap it with low and move low forward, also move mid forward
# if mid element is 1, move mid forward
# if mid element is 2, swap it with high and move high backwards
# stop when m > h because all those will be 2 itself
# logic: all elements to the left of l are 0
# logic: all elements to the right of r are 2
# logic: at the end, all elements from l to r are 1
"""
a = [0,1,2,0,1,2]
l=0
m=0
h=len(a)-1
while m <= h:
    if a[m] == 0:
        a[m], a[l] = a[l], a[m]
        m += 1
        l += 1
    elif a[m] == 1:
        m += 1
    elif a[m] == 2:
        a[m],a[h] = a[h],a[m]
        h -= 1
print(a)
"""
