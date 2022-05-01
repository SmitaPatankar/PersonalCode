# program: https://www.codingninjas.com/codestudio/problems/bubble-sort_980524
# program: bubble sort
# logic: create BUBBLE of 2 elements each time and move greater element forward so that each round puts one left over largest element towards the end
# first round sorts last element and so on, first element will already be sorted at end, so number of rounds = n - 1
# inside one more variable for start of bubble, start bubble at 0 and end at already sorted array - 1 i.e. n-i-1 because bubble consists of start and next element
# at the end all elements will be sorted
# chances are array gets sorted in between itself or is sorted at start itself in that case we dont need more rounds
# keep sorted flag as True for each round and make False when swap is needed, if True at end of round, skip other rounds and return
# time complexity: n-1 comparisons in first round, n-2,n-3....1 i.e. approx n(n+1)/2 i.e. O(n^2)
# space complexity: O(1)
# best case time complexity - already sorted - O(n) only one round
# use: in ith round we are getting ith largest element to its correct position
"""
def bubble_sort(a):
    sorted = True
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                sorted = False
                a[j], a[j+1] = a[j+1], a[j]
                print(a)
        if sorted:
            return
a = [8, 22, 7, 9, 31, 5, 13]
print(a)
bubble_sort(a)
print(a)
print()
a = [1,2,3,4,5,6]
print(a)
bubble_sort(a)
print(a)
"""

# hw: understand loop indexing started from 0
"""
no of rounds that is i should be 1 less than no of elements because leftmost element is already sorted towards the end
i.e. i=0, i<n-1,i++
for first round, start element of bubble will start from 0 till 2nd last element, coz last element will get included in bubble anyways as bubble is made up of 2 elements
for next round onwards, start element of bubble will start from 0 till no of elements - position of i - 1(for bubble end)
i.e. j=0,j<n-1-i,j++
"""

# hw: bubble sort is stable or unstable
"""
bubble sort is stable because swapping is done only when smaller element is backwards and greater element forward, swapping is not done when both elements are same, so they maintain order
eg: 0 2* 1* 2# 1#
0 1* 2* 1# 2#
0 1* 1# 2* 2#
"""

# hw: what is in place sort?
"""
when given array itself is modified without using additional space
"""

# hw: whether bubble sort is in place sort or not?
"""
bubble sort is in place because original array itself is modified without using additional space
"""

# hw: quiz: https://www.geeksforgeeks.org/quiz-bubblesort-gq/
"""
- best time complexity is O(n)

- best case is when array is already sorted in given order

- no of swappings for sorting 8, 22, 7, 9, 31, 5, 13 in asc is 9
8, 22, 7, 9, 31, 5, 13 --> question
8, 7, 22, 9, 31, 5, 13 --> 1
8, 7, 9, 22, 31, 5, 13 --> 2
8, 7, 9, 22, 5, 31, 13 --> 3
8, 7, 9, 22, 5, 13 || 31 --> 4
7, 8, 9, 22, 5, 13 || 31 --> 5
7, 8, 9, 5, 22, 13 || 31 --> 6
7, 8, 9, 5, 13|| 22 31 --> 7
7, 8, 5, 9, 13|| 22 31 --> 8
7, 5, 8, 9, || 13 22 31 --> 9
5, 7, 8, 9, || 13 22 31 --> 10 --> ans
"""
