it = (len(x) for x in open('015_multiple_conditions_in_list_comprehensions.py'))
print(it)
# <generator object <genexpr> at 0x05A63A30>

print(next(it))  # 36
print(next(it))  # 42

roots = ((x, x**0.5) for x in it)
print(next(roots))  # (43, 6.557438524302)
