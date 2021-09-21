# space optimization
# avoid redundant storage

# eg: similar first names and last names
# store at once place
# reference at multiple places

# eg: formatted character
# format ranges

import random
import string


class User:
    strings = []

    def __init__(self, full_name):
        def get_or_add_(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(s) - 1
        self.names = [get_or_add_(x) for x in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for _ in range(8)])


if __name__ == "__main__":
    users = []
    first_names = [random_string() for _ in range(100)]  # 100
    last_names = [random_string() for _ in range(100)]  # 100
    for first in first_names:
        for last in last_names:
            users.append(User(f"{first} {last}"))  # 10000
    print(users[5])
