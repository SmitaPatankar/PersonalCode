"""
divide and conquer
partition based on pivot number i.e. smaller than pivot and larger than pivot
repeat on left and right parition and so on until everything is sorted

pivot is the right most element

ideally pivot is random

no extra space needed

left and right marker move left until greater is found and move right until smaller is found and swap
then move left forward and if greater move right backward until small is found and swap
when left and right meet, swap that number with pivot

if left reaches pivot and right didnt move
pivot is sorted - reduce

O(NLOGN)
O(N)

needs space for recursion
it's not stable
"""

def partition(list, low, high):
    i = low - 1
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1           
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1] 
    return(i+1)

def quicksort(list, low, high):
    if low < high:
        pi = partition(list, low, high)
        quicksort(list, low, pi-1)
        quicksort(list, pi+1, high)
    return list

l = [3,2,7,6,10,9,8,5,4,1]
print(quicksort(l,0, 9))
