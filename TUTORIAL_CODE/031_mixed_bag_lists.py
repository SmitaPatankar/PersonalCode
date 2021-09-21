l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
# print(sorted(l))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unorderable types: str() < int()

print(sorted(l, key=int))
# [0, '1', 5, 6, '9', 14, 19, '23', 28, '28']
print(sorted(l, key=str))
# [0, '1', 14, 19, '23', 28, '28', 5, 6, '9']
'''
The sorting algorithm used in sorted and list.sort is Timsort, an adaptive algorithm that switches from insertion sort to merge sort strategies, depending on how ordered the data is. This is efficient because real-world data tends to have runs of sorted items. 
'''