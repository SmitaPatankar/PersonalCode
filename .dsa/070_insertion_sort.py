"""
take any element and insert at correct position

space efficiency

O(nsquare), O(1)
easy
for continuous inflow of numbers
"""

def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j>=0 and key<list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

print(insertionsort([3,4,1,2,5,6,7]))
