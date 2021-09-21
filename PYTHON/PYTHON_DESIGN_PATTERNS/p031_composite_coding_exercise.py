from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            for i in c:
                result += i
        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    pass


single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)

all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)
print(all_values.sum)
