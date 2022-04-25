# sorting details
"""
ascending/descending order
"""

# selection sort details
"""
in each round, select the smallest element and put it in right position
have a pointer for where to put the lowest element - it will be on 0 at start
put lowest value from entire including and further array over there by swapping and move the pointer forward
no need to sort last element i.e. n-1 rounds for n elements
use another pointer for finding lowest value
consider min as the current element index to begin with and then check further
"""

# program: https://www.codingninjas.com/codestudio/problems/selection-sort_981162
# program: selection sort
# space complexity - O(1) - constant - only variables made
# time complexity: n-1 -> n-2 -> n-3 ... 1 i.e. almost sum of 1 to n i.e. n(n+1)/2 i.e. n^2/2 + n/2 i.e. O(n^2)
# best case time complexity: O(n^2): we don't know where min is
# worst case time complexity: O(n^2): same as BigO notation
# application: when memory usage is restricted and array is small
"""
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [1,10,0,2,3,8]
print(arr)
selection_sort(arr)
print(arr)
"""

# hw: flowchart: selection sort
"""
start
input array
i = 0
if i < length of array - 1:
    min_index = i
    j = i + 1
    if j < length of array:
        if array[j] < array[min_index]:
            min_index = j
        j++
        continue
    else:
        go further
    swap array[i] and array[min_index]
    i++                        
    continue
else:
    go further
stop
"""

# hw: learn about stable(order preserving) and unstable algorithms
"""
stable sort
------------
if original array has duplicate elements, the sequence of those duplicate elements is maintained even after sorting
eg: 1 2* 3 2# 2$ should be sorted to 1 2* 2# 2$ 3 itself and these three 2's should not change positions

unstable sort
--------------
opposite of above

use of stable sort:
--------------------
col2 is sorted

col1    col2
1        a
2*       b
3        c
2#       d
2$       e

unstable sort col1 (messes up earlier col2 sorting)
col1    col2
1        a
2$       e -->
2#       d -->
2*       b -->
3        c

stable sort col1 (keeps earlier col2 sorting as intact as possible)
col1    col2
1        a
2*       b -->
2#       d -->
2$       e -->
3        c

Hence, use stable sorts where needed, else unstable sorts are fine too.
"""

# hw: check if selection sort is a stable algorithm
"""
selection sort is unstable sort
-----------------------------
we would think that because it always takes leftmost minimum element and put at left, sequence is maintained
but, that is wrong
what if while putting minimum element on left, some other duplicate element's left one ends in righter position due to swapping
hence selection sort is unstable
eg: 2a 4 3 2b 1
1 4 3 2b 2a
1 2b 3 4 2a
1 2b 2a 4 3
1 2b 2a 3 4
"""