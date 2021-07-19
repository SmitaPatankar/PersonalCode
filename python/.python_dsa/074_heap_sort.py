"""
insert to heap binary tree
extract to original array
"""

def heapify(customlist, n, i):
    smallest = i
    l = ((2 * i) + 1)
    r = ((2*i) + 2)
    if l < n and list[l] < list[r]:
        smallest = l
    if l < n and list[l] < list[r]:
        smallest = r
    if smallest != i:
        customlist[i], customlist[smallest] = customlist[smallest], customlist[i]
        heapify(customlist, n, smallest)

def heapsort(customlist):
    n = len(customlist)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customlist, n, i)
    for i in range(n-1,0,-1):
        customlist[i], customlist[0] = customlist[0], customlist[i]
        heapify(customlist,i,0)

print(heapsort([1,2,4,3,5,6,8,1]))
