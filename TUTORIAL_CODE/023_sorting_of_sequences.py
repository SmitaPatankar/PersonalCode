# This is an important Python API convention: functions or methods that change an object in place should return None to make it clear to the caller that the object itself was changed, and no new object was created.

'''
list.sort - same object
sorted(sequence) - new object

key and reverse - optional args
key - A one-argument function that will be applied to each item to produce its sorting key.
eg: key=str.lower, key=len

The key optional keyword parameter can also be used with the min() and max() built-ins and with other functions from the standard library (e.g., itertools.groupby() and heapq.nlargest())
'''


fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
# ['apple', 'banana', 'grape', 'raspberry']
print(fruits)
# ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, reverse=True))
# ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len))
# ['grape', 'apple', 'banana', 'raspberry']  # grape and apple are same len hence in original order
print(sorted(fruits, key=len, reverse=True))  # grape and apple are same len hence in original order
# ['raspberry', 'banana', 'grape', 'apple']
print(fruits)
# ['grape', 'raspberry', 'apple', 'banana']
print(fruits.sort())
# None
print(fruits)
# ['apple', 'banana', 'grape', 'raspberry']

