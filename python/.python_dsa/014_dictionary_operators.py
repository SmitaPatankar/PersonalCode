d = {1:2, 3:4, 5:6}

# check key
# time = O(1)
print(1 in d)

# check value
# time = O(1)
print(2 in d.values())

# loop with for
# time = O(n)
for k in d:
    print(k, d[k])
