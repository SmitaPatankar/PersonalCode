class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('Length is', len(foo))
foo.pop()
print('After pop:', repr(foo))
print('Frequency:', foo.frequency())

'''
Length is 7
After pop: ['a', 'b', 'a', 'c', 'b', 'a']
Frequency: {'a': 3, 'c': 1, 'b': 2}
'''


class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

bar = [1, 2, 3]
print(bar[0])
# it will be interpreted as:
bar.__getitem__(0)


class IndexableNode(BinaryNode):
    def _search(self, count, index):
        pass # ...
        # Returns (found, count)

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value


tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6, right=IndexableNode(7))),
    right=IndexableNode(
        15, left=IndexableNode(11)))

print('LRR =', tree.left.right.right.value)
print('Index 0 =', tree[0])
print('Index 1 =', tree[1])
print('11 in the tree?', 11 in tree)
print('17 in the tree?', 17 in tree)
print('Tree is', list(tree))

'''
LRR = 7
Index 0 = 2
Index 1 = 5
11 in the tree? True
17 in the tree? False
Tree is [2, 5, 6, 7, 10, 11, 15]
'''

# The problem is that implementing __getitem__ isn’t enough to provide
# all of the sequence semantics you’d expect.


# len(tree)
# TypeError: object of type 'IndexableNode' has no len()

class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count


tree = SequenceNode('pass# ...')

print('Tree has %d nodes' % len(tree))
# Tree has 7 nodes

# Also missing are the count and index methods that a Python programmer
# would expect to see on a sequence like list or tuple.
# Defining your own container types is much harder than it looks.

from collections.abc import Sequence


class BadType(Sequence):
    pass


foo = BadType()


# TypeError: Can't instantiate abstract class BadType with abstract methods __getitem__, __len__
# When you do implement all of the methods required by an abstract base class,
# as I did above with SequenceNode, it will provide all of the additional
# methods like index and count for free.

class BetterNode(SequenceNode, Sequence):
    pass


tree = BetterNode(
    'pass # ...'
)

print('Index of 7 is', tree.index(7))
print('Count of 10 is', tree.count(10))

'''
Index of 7 is 3
Count of 10 is 1
'''
