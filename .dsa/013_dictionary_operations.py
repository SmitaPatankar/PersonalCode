# unordered - LEARN MORE
# changeable
# indexed by key
# no duplicates
# misc info:
#     considers float and int as int key - d{1:2,1.0:5} - d{1:5}
#     considers list of key search as tuple key - d[1,2] - d[(1,2)]

# create
# time = O(n)
# space = O(n)
d = dict()
print(d)

d = {}
print(d)

d = {"smile": "be happy", "cry": "be sad"}
print(d)

# access
# time = O(1)
# space = O(1)
print(d["smile"])

# memory storage
# index of kv pair is obtained by applying hash function on key
# stored in hash table
# in case of collision, second kv pair is added as linked list at the end of first kv pair

# update
# time = O(1)
# space = O(1)
d = {1:2, 3:4, 5:6}
d[1] = 5
print(d)

# add
# time = O(1) - LEARN MORE
# space = O(1) - LEARN MORE
d[6] = 7
print(d)

# traverse
# time = O(n)
# space - O(1)
for k in d:
    print(k, d[k])

# search value
# time = O(n)
# space - O(1)
def search(d, v):
    for k in d:
        if d[k] == v:
            return k
    return "not found"
print(search({1:2, 3:4, 5:6, 7: 7}, 7))

# delete specific key
# time = O(1) - LEARN MORE
# space = O(1) - LEARN MORE
print(d.pop(1))
print(d)

# delete random key
# time = O(1) or O(n) - LEARN MORE
# space = O(1) - LEARN MORE
print(d.popitem())
print(d)

# delete all keys
# time = O(1) or O(n) - LEARN MORE
# space = O(1) - LEARN MORE
d.clear()
print(d)

# delete certain key
# time = O(1) or O(n) - LEARN MORE
# space = O(1) - LEARN MORE
d = {1:2,2:3}
del d[2]
print(d)

# create copy
dd = d.copy()
print(dd)

# create dict from keys and common value
d = dict.fromkeys([1,2,3,4,5], "common")
print(d)

# get value for key
# if key found, value is returned
# if key not found and custom value is specified, that is returned
# if key not found and custom value is not specified, ddefault value of None is returned
print(d.get(2))
print(d.get(15, "not found"))
print(d.get(15))

# get list of tuples of kv pairs (as view obj)
print(d.items())

# get list of keys (as view obj)
print(d.keys())

# get list of values (as view obj)
print(d.keys())

# set default
# if key exists, its value will be returned
# if key does not exist and default value is not provided, value will be set and returned as null
# if key does not exist and default value is provided, value will be set and returned as that default value
print(d.setdefault(2, "two"))
print(d)
print(d.setdefault(10))
print(d)
print(d.setdefault(20, "twenty"))
print(d)

# update from another dict or list of tuple kv pairs (if key exists, value will be replaced, else kv pair will be added)
d = {1:2}
d.update({3:4})
print(d)
d.update({3:5})
print(d)
d.update([(1,10)])
print(d)

# search key
# time = O(1)
# space = O(1)
print(1 in {1:2, 3:4})
