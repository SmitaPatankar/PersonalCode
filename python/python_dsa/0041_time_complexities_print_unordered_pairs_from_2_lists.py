def printUnorderedPairs(lst1, lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] < lst2[j]:
                print(str(lst1[i]) + "," + str(lst2[j]))

printUnorderedPairs([1,2,3,4,5],[2,6,7,8])

# O(mn)
