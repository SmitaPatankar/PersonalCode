def find_biggest(lst, n):
    if n == 1:
        return lst[0]
    return max(lst[n-1], find_biggest(lst, n-1))

print(find_biggest([1,2,3,10,-1], 5))
