def normalize(numbers):
    print('there1')
    total = sum(numbers)
    result = []
    print('there2')
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        print('here')
        with open(self.data_path) as f:
            print('file opened')
            for line in f:
                yield int(line)


visits = ReadVisits('my_numbers.txt')
percentages = normalize(visits)
print(percentages)

'''
there1
here
file opened
there2
here
file opened
[6.666666666666667, 13.333333333333334, 20.0, 26.666666666666668, 33.333333333333336]
'''
