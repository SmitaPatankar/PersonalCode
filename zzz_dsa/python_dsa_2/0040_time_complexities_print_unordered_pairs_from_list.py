def printUnorderedPairs(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            print(lst[i] + "," + lst[j])

printUnorderedPairs(["1","2","3","4","5"])

# O(n^2)
