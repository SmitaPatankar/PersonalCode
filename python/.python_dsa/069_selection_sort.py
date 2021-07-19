"""
select minimum element and put at start

if data is already ok
O(nsquare), O(1)

easy

poor time
"""
def selectionsort(list):
    for i in range(len(list)):
        minindex = i
        for j in range(i, len(list)):
            if list[j] < list[minindex]:
                minindex = j
        list[i], list[minindex] = list[minindex], list[i]         

l = [4,2,3,0,1,5,6,8,7,9]
selectionsort(l)
print(l)
