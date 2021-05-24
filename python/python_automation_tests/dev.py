import os
import random


def get_random_digital_string(start, end):
    return str(random.randint(start, end))


def get_capitalized_env_name():
    return os.environ["name"].upper()


class C:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_random_number(self):
        return random.randint(self.start, self.end)

    def get_random_digital_string(self):
        return str(self.get_random_number())
