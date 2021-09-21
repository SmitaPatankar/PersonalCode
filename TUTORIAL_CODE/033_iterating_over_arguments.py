def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)  # []

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))
# [1, 2, 3, 4, 5]
# []


def normalize_copy(numbers):
    numbers = list(numbers)  # Copy the iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)  #  [6.666666666666667, 13.333333333333334, 20.0, 26.666666666666668, 33.333333333333336]
