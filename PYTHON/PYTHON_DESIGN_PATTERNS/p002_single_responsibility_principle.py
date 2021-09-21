# single responsibility
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        return "\n".join(self.entries)


# single responsibility
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))
            f.close()


j = Journal()
j.add_entry("drank water")
j.add_entry("learnt something")
print(f"journal entries from object:\n{j}")

fp = "C://SMITA PERSONAL REPOSITORY//GITHUB CODE//.temp/dummy.txt"

p = PersistenceManager()
p.save_to_file(j, fp)

with open(fp, "r") as f:
    print(f"journal entries from file:\n{f.read()}")
