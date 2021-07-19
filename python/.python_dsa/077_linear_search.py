def linearsearch(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1

print(linearsearch([6,7,5,4,2], 5))
print(linearsearch([6,7,5,4,2], 10))
