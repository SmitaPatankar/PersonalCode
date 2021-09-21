a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = map(lambda x: x ** 2, a)
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
