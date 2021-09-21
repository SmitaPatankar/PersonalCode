def sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i][i]
    return total

lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(sum(lst))
