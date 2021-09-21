class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def get_hash(self, key):
        sum = 0
        for chr in key:
            sum += ord(chr)
        return sum % self.size

    def add(self, key, value):
        hash = self.get_hash(key)
        key_value = [key, value]
        if not self.map[hash]:
            self.map[hash] = [key_value]
            return True
        for lst in self.map[hash]:
            if lst[0] == key:
                lst[1] = value
                return True
        self.map[hash].append(key_value)
        return True

    def get(self, key):
        hash = self.get_hash(key)
        if self.map[hash]:
            for pair in self.map[hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        hash = self.get_hash(key)
        if not self.map[hash]:
            return False
        for i in range(len(self.map[hash])):
            if self.map[hash][i][0] == key:
                self.map[hash].pop(i)
                return True
        return False

    def keys(self):
        k = []
        for i in range(0, self.size):
            if self.map[i]:
                for lst in self.map[i]:
                    k.append(lst[0])
        return k

    def print(self):
        for lst in self.map:
            if lst:
                print(lst, end="  ")
        print()


print("creating hashmap i.e. list of Nones upto size---------->")
h = HashMap()
h.print()

print("adding kv pair---------->")
h.add("smita", "patankar")
h.print()

print("adding kv pair with same key---------->")
h.add("smita", "myupdatedsurname")
h.print()

print("adding kv pair with same hash---------->")
h.add("atims", "raknatap")
h.print()

print("adding kv pair with diff hash---------->")
h.add("neha", "patankar")
h.print()

print("getting value for key---------->")
print(h.get("smita"))
print(h.get("atims"))
print(h.get("neha"))
print(h.get("wrong"))

print("getting keys---------->")
print(h.keys())

print("deleting kv pair---------->")
h.delete("atims")
h.print()
h.delete("smita")
h.print()
h.delete("neha")
h.print()
h.delete("wrong")
h.print()
