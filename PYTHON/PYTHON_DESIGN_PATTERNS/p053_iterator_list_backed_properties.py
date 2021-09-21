class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[self._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def agility(self):
        return self.stats[self._agility]

    @property
    def intelligence(self):
        return self.stats[self._intelligence]

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stats(self):
        return max(self.stats)
