def printPairs(lst):
    for i in lst:
        for j in lst:
            print(str(i)+","+str(j))

printPairs([1,2,3,4,5])

# O(n^2)
