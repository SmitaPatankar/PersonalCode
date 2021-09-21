from collections import defaultdict

'''
For example, the list type’s sort method takes an optional key argument
that’s used to determine each index’s value for sorting.
Here, I sort a list of names based on their lengths by providing a
lambda expression as the key hook:
'''

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)  # ['Plato', 'Socrates', 'Aristotle', 'Archimedes']

def log_missing():
   print('Key added')
   return 0

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))

'''
Before: {'green': 12, 'blue': 3}
Key added
Key added
After:  {'orange': 9, 'green': 12, 'blue': 20, 'red': 5}
'''

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2

'''
The problem with defining a closure for stateful hooks is that it’s harder
to read than the stateless function example. Another approach is
to define a small class that encapsulates the state you want to track.
'''

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current)  # Method ref

for key, amount in increments:
    result[key] += amount
assert counter.added == 2

# but not clear

# Python allows classes to define the __call__ special method.
# __call__ allows an object to be called just like a function.
# It also causes the callable built-in function to return True for such an instance.

class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)

counter = BetterCountMissing()
result = defaultdict(counter, current)  # Relies on __call__
for key, amount in increments:
    result[key] += amount
assert counter.added == 2

# It provides a strong hint that the goal of the class is to act as a stateful closure.

# When you need a function to maintain state, consider defining a class that
# provides the __call__ method instead of defining a stateful closure
