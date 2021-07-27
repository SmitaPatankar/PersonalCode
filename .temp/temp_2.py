def get_unique_list(lst):
    return list(set(lst))

print(get_unique_list(['a','b','c','d','d','d','e','a','b','f','g','g','h']))
# ['a', 'h', 'd', 'g', 'f', 'e', 'c', 'b']
