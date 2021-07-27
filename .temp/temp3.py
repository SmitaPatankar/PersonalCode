def find_second_largest(lst):
    max = 0
    second_max = 0
    for n in lst:
        if n > max:
            second_max = max
            max = n
        elif n > second_max:
            second_max = n
    return second_max

print(find_second_largest([10,90,2,5,66,77,91,100,76,1000]))
# 100
