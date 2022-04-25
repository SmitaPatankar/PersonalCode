class Hashtable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value)
                while (
                    self.slots[next_slot] is not None and self.slots[next_slot] != key
                ):
                    next_slot = self.rehash(next_slot)
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash_function(key)
        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


h = Hashtable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
print(h.slots)
print(h.data)
print(h[20])
print(h[17])
print(h[20])
print(h.data)
print(h[99])

# todo
"""
Dealing with the situation where there are no empty slots left is an exercise.

We leave the remaining methods as exercises.
"""
