"""
create buckets
distribute elements
sort buckets
merge buckets

no of buckets = round(sqrt(noofelements))
appropriate bucket for an element = ceil(value * no of buckets / maxvalue)

use when numbers are uniformly distributed

needs space
"""

import math

q = __import__("073_quick_sort")

def bucketsort(list):
    noofbuckets = round(math.sqrt(len(list)))
    maxvalue = max(list)
    arr = []  # space O(N)
    for _ in range(noofbuckets):
        arr.append([])
    for j in list:
        index_b = math.ceil(j * noofbuckets / maxvalue)
        arr[index_b - 1].append(j)
    for i in range(noofbuckets):
        arr[i] = q.quicksort(arr[i], 0, len(arr[i])-1)  # time O(NLOGN)
    k = 0
    for i in range(noofbuckets):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k += 1
    return list

l = [5,6,1,7,2,3,4]
print(bucketsort(l))
