def isUnique(list):
  visited=[]
  for i in list:
    if i in visited:
        print(i)
        return False
    else:
        visited.append(i)
  return True

print(isUnique([1,2,3,4,5]))
