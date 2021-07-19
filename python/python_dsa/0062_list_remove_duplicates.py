def removeDuplicates(myList):
    visited=[]
    for i in myList:
        if i not in visited:
            visited.append(i)
    return visited

print(removeDuplicates([1,2,3,3,2,1]))
