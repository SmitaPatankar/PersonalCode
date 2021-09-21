class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
print(normalize_defensive(visits))  # [11.538461538461538, 26.923076923076923, 61.53846153846154]
visits = ReadVisits('my_numbers.txt')
print(normalize_defensive(visits))  # [6.666666666666667, 13.333333333333334, 20.0, 26.666666666666668, 33.333333333333336]
it = iter(visits)
normalize_defensive(it)  # TypeError: Must supply a container
