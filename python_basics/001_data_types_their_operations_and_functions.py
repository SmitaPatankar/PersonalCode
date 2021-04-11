# float
# 1.0 -> 1.0

# int
# 1 -> 1

# int operations
# 1+1 -> 2
# 1*3 -> 3
# 1/2 -> 0.5
# 2**4 -> 16
# 4 % 2 -> 0

# precedence of int operations
# 2 + 3 * 5 + 5 -> 22
# (2+3) * (5+5) -> 50

# int variables
# x = 2
# y = 3

# operations on int variables
# x+y -> 5
# x = x+x
# x -> 4

# string
# 'smita' -> 'smita'
# "smita" -> 'smita'
# "I can't go" -> "I can't go"
# 'smita said "hi"' -> 'smita said "hi"'

# string variable
# x = 'hello'
# x -> 'hello'
# print(x) -> hello

# string formatting
# num = 12
# name = "sam"
# 'my number is {} and my name is {}'.format(num, name) -> 'my number is 12 and my name is sam'
# 'my number is {one} and my name is {two}. hey my name is {two}'.format(two=name, one=num) -> 'my number is 12 and my name is sam. hey my name is sam'

# string functions
# s = "hello my name is Sam"
# s.lower() -> 'hello my name is sam'
# s.upper() -> 'HELLO MY NAME IS SAM'
# s.split() -> ['hello', 'my', 'name', 'is', 'Sam']
# s.split("m") -> ['hello ', 'y na, 'e is Sa']

# string indexing
# s = "abcdefghijk"
# s[0] -> 'a'
# s[4] -> 'e'

# string slicing
# s[0:] -> 'abcdefghijk'
# s[:3] -> 'abc'
# s[0:3] -> 'abc'
# s[3:6] -> 'def'

# list
# ['a', 'b', 'c'] -> ['a', 'b', 'c']
# [1,2,3] -> [1,2,3]

# list variable
# l = ['a', 'b', 'c']

# list functions
# l.append('d')
# l -> ['a', 'b', 'c', 'd']
# l.pop() -> 'd'
# l -> ['a', 'b', 'c']
# l.pop(0) -> 'a'
# l -> ['b', 'c']

# list indexing
# l[0] -> 'a'

# list item reassignment
# l[0] = 'new'
# l -> ['new', 'b', 'c', 'd']

# list slicing
# l[1:3] -> ['b', 'c']

# in operation on list
# 'b' in l -> True
# 'd' in l -> False

# nested lists
# nest = [1,2, [3,4]]
# nest[2] -> [3,4]
# nest[2][1] -> 4

# dictionary
# d = {'key1': 'value', 'key2': 123}
# d['key1'] -> 'value'
# d['key2'] -> 123
# d = {'k1': [1,2,3]}
# d -> {'k1': [1,2,3]}
# d["k1"] -> [1,2,3]
# d["k1"][1] -> 2
# d = {"k1":{"innerkey":[1,2,3]}}
# d["k1"]["innerkey"][1] -> 2

# dictionary functions
# d.keys() -> dict_keys(['k1'])
# d.values() -> dict_values(['innerkey': [1,2,3]])
# d.items() -> dict_items([('k1': {'innerkey': [1,2,3]})])

# boolean
# True -> True
# False -> False

# tuple
# (1,2,3) -> (1,2,3)

# tuple variable
# t = (1,2,3)

# tuple indexing
# t[0] -> 1

# tuple item reassignment
# t[0] = 'New' # TypeError: 'tuple' object does not support item assignment

# tuple unpacking
# l = [(1,2), (3,4), (5,6)]
# for a,b in l:
#     print(a) --> 1 {newline} 3 {newline} 5

# set
# {1,2,3} -> {1,2,3}
# {1,2,1,2,3,1,2} -> {1,2,3}
# set([1,2,3,1,2,3]) -> {1,2,3}

# set variable
# s = {1,2,3}

# set operations
# s.add(5)
# s -> {1,2,3,5}
# s.add(5)
# s -> {1,2,3,5}

# comparison operations
# 1>2 -> False
# 1<2 -> True
# 1>=2 -> False
# 1<=2 -> True
# 1==2 -> False
# 1!=2 -> True
# 'hi' == 'bye' -> False
# 'hi' != 'bye' -> True
# 1<2 and 2<3 -> True
# 1<2 and 2>3 -> False
# 1<2 or 2>3 -> True
# True and True -> True
# True and False -> False
# True or True -> True
# True or False -> True