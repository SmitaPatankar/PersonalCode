# find minimum number
# compare everything to everything
"""
def findmin(lst):
    for i in lst:
        min = True
        for j in lst:
            if i > j:
                min = False
        if min:
            return i
print(findmin([0,1,24,8,19,-2,22,-1]))
"""

# find minimum number
# linear
"""
def min(lst):
    min = lst[0]
    for n in lst:
        if n < min:
            min = n
    return min
print(min([0,1,24,8,19,-2,22,-1]))
"""
