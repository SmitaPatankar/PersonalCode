def find_biggest(lst):
    max = lst[0]
    for element in lst[1:]:
        if element > max:
            max = element
    return(max)

print(find_biggest([1,2,3,10,-1]))
