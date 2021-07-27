# key value pair
# add - new hash
# add - same hash same key
# add - same hash new key
# get
# delete

class HashMap:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for chr in key:
            hash += ord(chr)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if not self.map[key_hash]:
            self.map[key_hash] = list([key_value])
            return True
        for pair in self.map[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.map[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash]:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if not self.map[key_hash]:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def print(self):
        for pair in self.map:
            if pair:
                print(pair)

print("create")
map = HashMap()
map.print()

print("add")
map.add("smita", "patankar")
map.print()

print("add")
map.add("smita", "surname")
map.print()

print("add")
map.add("ravi", "lohot")
map.print()

print("add")
map.add("asmit", "rapatank")
map.print()

print("get")
print(map.get("smita"))

print("get")
print(map.get("ravi"))

print("get")
print(map.get("asmit"))

print("get")
print(map.get("blah"))

print("delete")
print(map.delete("asmit"))
map.print()

print("delete")
print(map.delete("ravi"))
map.print()

print("delete")
print(map.delete("tisma"))
map.print()

print("delete")
print(map.delete("blah"))
map.print()
