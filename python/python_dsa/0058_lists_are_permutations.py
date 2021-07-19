def permuntation(list1, list2):
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

print(permuntation([1,2,3], [3,2,1]))
