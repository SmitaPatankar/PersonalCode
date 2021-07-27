import math
def binarysearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    print(start, middle, end)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1

l = [0,1,2,3,4,5,6,7,8,9]
print(l)
print(binarysearch(l, -100))
