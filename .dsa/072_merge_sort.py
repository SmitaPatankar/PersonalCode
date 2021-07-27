"""
divide recursively
merge by sorting

O(nlogn), O(n)

stable
"""

def merge(list, l, m , r):
    n1 = m -l + 1
    n2 = r - m
    L = [0] * n1    
    R = [0] * n2
    for i in range(0, n1):
        L[i] = list[l+i]    
    for j in range(0, n2):
        R[j] = list[m+1+j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        list[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        list[k] = R[j]
        j += 1
        k += 1

def mergesort(list, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergesort(list, l, m)
        mergesort(list, m+1, r)
        merge(list, l, m, r)
    return list

l = [9,8,7,6,5,3,4,2,1]
print(mergesort(l, 0, 8))
