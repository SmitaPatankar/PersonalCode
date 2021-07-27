d1 = {"k1": "v1", "k2": "v2", "k3": "v3"}
d2 = {"k1": "v1", "k2": "v2", "k4": "v4"}

# common keys
# unique keys in d1
# unique keys in d2

# print("common")
# print(set(d1.keys()).intersection(set(d2.keys())))

# print("unique for d1")
# print(set(d1.keys()).difference(set(d2.keys())))

# print("unique for d2")
# print(set(d2.keys()).difference(set(d1.keys())))

# common_keys = []
# d1_unique_keys = []
# d2_unique_keys = []

print("common for d1 and d2")
print([k for k in d1.keys() if k in d2.keys()])

print("d1 unique")
print([k for k in d1.keys() if k not in d2.keys()])

print("d2 unique")
print([k for k in d2.keys() if k not in d1.keys()])