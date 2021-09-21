from itertools import islice


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


address = 'Four score and seven years ago...'
result = list(index_words_iter(address))


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('030_nonlocal_alternative_for_python2.py', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))   # [0, 4, 27]
