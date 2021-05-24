from collections import namedtuple


def m():
    return namedtuple("data", ["a", "b", "c"])(1, 2, 3)


results = m()
print(results.b)  # 2
