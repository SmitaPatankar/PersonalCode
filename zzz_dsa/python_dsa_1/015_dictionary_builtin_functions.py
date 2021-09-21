# all - whether all keys in dict are true or not - works on iterable
# true for empty dict also
print(all({}))
d = {0:1, 1:1}
print(all(d))
d = {1:0, 2:0}
print(all(d))

# any - whether any key in dict is true or not - works on iterable
# false for empty dict also
print(any({}))
d = {0:1, 1:1}
print(any(d))
d = {1:0, 2:0}
print(any(d))

# length - works on collection of items
print(len(d))

# get list of sorted keys - works on iterable
# optional - reverse parameter - boolean - false by default
# optional - key parameter for sorting - None by default
d = {"44":1, "33":2, "2":1, "1":0}
print(sorted(d))
print(sorted(d, reverse=True))
print(sorted(d, key=len))
