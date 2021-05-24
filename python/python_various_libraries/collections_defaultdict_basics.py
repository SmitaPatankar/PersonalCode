from collections import defaultdict

d = defaultdict(set)

print(d)
# defaultdict(<class 'set'>, {})

print(d["a"])
# set()

d["a"].add(0)
print(d)
# defaultdict(<class 'set'>, {'a': {0}})

d["a"].add(1)
print(d)
# defaultdict(<class 'set'>, {'a': {0, 1}})
