# compare 2 elements in pair to each other and move forward and sort, at the end, last element is sorted
# repeat on all other elements

# if data is already ok
# for space concern
# easy implementation

# poor time

# learn more about direct swapping in python

# O(n^2), O(1)
def bubblesort(list):
    for i in range(len(list) - 1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

l = [5,4,3,2,1,0,-1,9,8,7,6,33,100,-5]
bubblesort(l)
print(l)
