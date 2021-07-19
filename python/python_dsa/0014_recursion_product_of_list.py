def product(lst, n):
    if n == 0:
        return 1
    return lst[0] * product(lst[1:], n-1)

print(product([1,2,3,10], 4))
