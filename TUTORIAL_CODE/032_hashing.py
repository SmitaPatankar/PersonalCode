from collections import abc

my_dict = {}
isinstance(my_dict, abc.Mapping)

tt = (1, 2, (30, 40))
print(hash(tt))

# 8027212646858338501

tl = (1, 2, [30, 40])
# print(hash(tl))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))
# -4118419923444501110

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
# True

# dict comprehension

DIAL_CODES = [(86, 'China'), (91, 'India')]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
'''
{'China': 86, 'India': 91, 'Bangladesh': 880, 'United States': 1,
'Pakistan': 92, 'Japan': 81, 'Russia': 7, 'Brazil': 55, 'Nigeria':
234, 'Indonesia': 62}
'''

print({code: country.upper() for country, code in country_code.items() if code < 66})
# {1: 'UNITED STATES', 55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA'}

# not oprtimized

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])

# better

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])

# same as below but better

# if key not in my_dict:
#     my_dict[key] = []
# my_dict[key].append(new_value)

# A defaultdict is configured to create items on demand whenever a missing key is searched.

'''
For example, given an empty defaultdict created as dd = defaultdict(list), if 'new-key' is not in dd, the expression dd['new-key'] does the following steps:

Calls list() to create a new list.

Inserts the list into dd using 'new-key' as key.

Returns a reference to that list.

The callable that produces the default values is held in an instance attribute called default_factory.
'''

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])

# The default_factory of a defaultdict is only invoked to provide default values for __getitem__ calls, and not for the other methods. For example, if dd is a defaultdict, and k is a missing key, dd[k] will call the default_factory to create a default value, but dd.get(k) still returns None.

'''
the __missing__ method is just called by __getitem__ (i.e., for the d[k] operator). The presence of a __missing__ method has no effect on the behavior of other methods that look up keys, such as get or __contains__ (which implements the in operator). This is why the default_factory of defaultdict works only with __getitem__
'''

class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
# 'two'
print( d[4])
# 'four'
print(d[1])
# Traceback(most recent call last):
# ...
# KeyError: '1'

d.get('2')
# 'two'
d.get(4)
# 'four'
d.get(1, 'N/A')
# 'N/A'

print(2 in d)
# True
print(1 in d)
# False

'''
A search like k in my_dict.keys() is efficient in Python 3 even for very large mappings because dict.keys() returns a view, which is similar to a set, and containment checks in sets are as fast as in dictionaries. Details are documented in the “Dictionary” view objects section of the documentation. In Python 2, dict.keys() returns a list, so our solution also works there, but it is not efficient for large dictionaries, because k in my_list must scan the list.
'''

# collections.OrderedDict

# list of mapping can be searched as one
from collections import ChainMap
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))

# A mapping that holds an integer count for each key.
# Updating an existing key adds to its count.

ct = collections.Counter('abracadabra')
print(ct)
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')
print(ct)
# Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.most_common(2)
# [('a', 10), ('z', 3)]

# collections.UserDict
# A pure Python implementation of a mapping that works like a standard dict.

'''
The main reason why it’s preferable to subclass from UserDict rather than from dict is that the built-in has some implementation shortcuts that end up forcing us to override methods that we can just inherit from UserDict with no problems.
'''

import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# UserDict subclasses MutableMapping

# MutableMapping.update
# Mapping.get

# MappingProxyType builds a read-only mappingproxy instance from a dict

from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
# mappingproxy({1: 'A'})
print(d_proxy[1])
# 'A'
# d_proxy[2] = 'x'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
print(d_proxy)
# mappingproxy({1: 'A', 2: 'B'})
print(d_proxy[2])
# 'B'

# A set is a collection of unique objects. A basic use case is removing duplication:

l = ['spam', 'spam', 'eggs', 'spam']
print(set(l))
# {'eggs', 'spam'}
print(list(set(l)))
# ['eggs', 'spam']

# Set elements must be hashable. The set type is not hashable, but frozenset is, so you can have frozenset elements inside a set.
# a | b returns their union, a & b computes the intersection, and a - b the difference

# found = len(needles & haystack)
# else
'''
found = 0
for n in needles:
    if n in haystack:
        found += 1
'''
# for something other than sets, create sets on the fly
'''
found = len(set(needles) & set(haystack))

# another way:
found = len(set(needles).intersection(haystack))
'''

# set() - empty set
# {} - empty dict

s = {1}
print(type(s))
# <class 'set'>
print(s)
# {1}
print(s.pop())
# 1
print(s)
# set()

# to process a literal like {1, 2, 3}, Python runs a specialized BUILD_SET bytecode
# (e.g., set([1, 2, 3])). The latter form is slower because, to evaluate it, Python has to look up the set name to fetch the constructor, then build a list, and finally pass it to the constructor.

# dis.dis (the disassembler function)

from dis import dis
dis('{1}')
'''
  1           0 LOAD_CONST               0 (1)
              3 BUILD_SET                1
              6 RETURN_VALUE
'''
dis('set([1])')
'''
  1           0 LOAD_NAME                0 (set)
              3 LOAD_CONST               0 (1)
              6 BUILD_LIST               1
              9 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             12 RETURN_VALUE
'''

frozenset(range(10))
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

# setcomp

from unicodedata import name
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')})
# {'§', '=', '¢', '#', '¤', '<', '¥', 'µ', '×', '$', '¶', '£', '©', '°', '+', '÷', '±', '>', '¬', '®', '%'}

# add, discard, remove, pop, clear
# a.union(b,c,d) - only a needs to be set, rest could be anything
# many methods
'''
s.pop()
Remove and return an element from s, raising KeyError if s is empty
s.remove(e)
Remove element e from s, raising KeyError if e not in s
s.discard(e)
Remove element e from s if it is present
s.__iter__()
Get iterator over s
'''

# found = 0
# for n in needles:
#     if n in haystack:
#         found += 1
# found = len(needles & haystack) # set

# there is no hash table to support searches with the in operator on a list, so a full scan must be made, resulting in times that grow linearly with the size of the haystack.

'''
A hash table is a sparse array (i.e., an array that always has empty cells). In standard data structure texts, the cells in a hash table are often called “buckets.” In a dict hash table, there is a bucket for each item, and it contains two fields: a reference to the key and a reference to the value of the item. Because all buckets have the same size, access to an individual bucket is done by offset.
Python tries to keep at least 1/3 of the buckets empty; if the hash table becomes too crowded, it is copied to a new location with room for more buckets.
To put an item in a hash table, the first step is to calculate the hash value of the item key, which is done with the hash() built-in function, explained next.
'''

# 1 == 1.0 is true, hash(1) == hash(1.0)

# Starting with Python 3.3, a random salt value is added to the hashes of str, bytes, and datetime objects. The salt value is constant within a Python process but varies between interpreter runs. The random salt is a security measure to prevent a DOS attack.

'''
THE HASH TABLE ALGORITHM
To fetch the value at my_dict[search_key], Python calls hash(search_key) to obtain the hash value of search_key and uses the least significant bits of that number as an offset to look up a bucket in the hash table (the number of bits used depends on the current size of the table). If the found bucket is empty, KeyError is raised. Otherwise, the found bucket has an item—a found_key:found_value pair—and then Python checks whether search_key == found_key. If they match, that was the item sought: found_value is returned.

However, if search_key and found_key do not match, this is a hash collision. This happens because a hash function maps arbitrary objects to a small number of bits, and—in addition—the hash table is indexed with a subset of those bits. In order to resolve the collision, the algorithm then takes different bits in the hash, massages them in a particular way, and uses the result as an offset to look up a different bucket.8 If that is empty, KeyError is raised; if not, either the keys match and the item value is returned, or the collision resolution process is repeated. 
'''

'''
The process to insert or update an item is the same, except that when an empty bucket is located, the new item is put there, and when a bucket with a matching key is found, the value in that bucket is overwritten with the new value.Additionally, when inserting items, Python may determine that the hash table is too crowded and rebuild it to a new location with more room. As the hash table grows, so does the number of hash bits used as bucket offsets, and this keeps the rate of collisions low.
'''

'''
If you implement a class with a custom __eq__ method, and you want the instances to be hashable, you must also implement a suitable __hash__, to make sure that when a == b is True then hash(a) == hash(b) is also True. Otherwise you are breaking an invariant of the hash table algorithm, with the grave consequence that dicts and sets will not handle your objects reliably. On the other hand, if a class has a custom __eq$__ that depends on mutable state, its instances are not hashable and you must never implement a __hash__ method in such a class.
'''

'''
For example, if you are handling a large quantity of records, it makes sense to store them in a list of tuples or named tuples instead of using a list of dictionaries in JSON style, with one dict per record. Replacing dicts with tuples reduces the memory usage in two ways: by removing the overhead of one hash table per record and by not storing the field names again with each record.

For user-defined types, the __slots__ class attribute changes the storage of instance attributes from a dict to a tuple in each instance. This will be discussed in “Saving Space with the __slots__ Class Attribute” (Chapter 9).

Keep in mind we are talking about space optimizations. If you are dealing with a few million objects and your machine has gigabytes of RAM, you should postpone such optimizations until they are actually warranted. Optimization is the altar where maintainability is sacrificed.
'''

'''
When a hash collision happens, the second key ends up in a position that it would not normally occupy if it had been inserted first. So, a dict built as dict([(key1, value1), (key2, value2)]) compares equal to dict([(key2, value2), (key1, value1)]), but their key ordering may not be the same if the hashes of key1 and key2 collide.
'''

DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3

# d1: dict_keys([880, 1, 86, 55, 7, 234, 91, 92, 62, 81])
# d2: dict_keys([880, 1, 91, 86, 81, 55, 234, 7, 92, 62])
# d3: dict_keys([880, 81, 1, 86, 55, 7, 234, 91, 92, 62])

'''
Whenever you add a new item to a dict, the Python interpreter may decide that the hash table of that dictionary needs to grow. This entails building a new, bigger hash table, and adding all current items to the new table. During this process, new (but different) hash collisions may happen, with the result that the keys are likely to be ordered differently in the new hash table. All of this is implementation-dependent, so you cannot reliably predict when it will happen. If you are iterating over the dictionary keys and changing them at the same time, your loop may not scan all the items as expected—not even the items that were already in the dictionary before you added to it.

This is why modifying the contents of a dict while iterating through it is a bad idea. If you need to scan and add items to a dictionary, do it in two steps: read the dict from start to finish and collect the needed additions in a second dict. Then update the first one with it.
'''

'''
In Python 3, the .keys(), .items(), and .values() methods return dictionary views, which behave more like sets than the lists returned by these methods in Python 2. Such views are also dynamic: they do not replicate the contents of the dict, and they immediately reflect any changes to the dict.
'''

'''
The set and frozenset types are also implemented with a hash table, except that each bucket holds only a reference to the element (as if it were a key in a dict, but without a value to go with it). In fact, before set was added to the language, we often used dictionaries with dummy values just to perform fast membership tests on the keys.
Set elements must be hashable objects.

Sets have a significant memory overhead.

Membership testing is very efficient.

Element ordering depends on insertion order.

Adding elements to a set may change the order of other elements.
'''

