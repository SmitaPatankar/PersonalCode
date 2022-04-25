# add item to list
# O(n)
l = []
for i in range(1000):
    l = l + [i]
# add item to list
# O(1)
l = []
for i in range(1000):
    l = l.append(i)
# add item to list
# list comprehension
l = [x for x in range(1000)]
# add item to list
# range
l = list(range(1000))

# todo
# https://runestone.academy/runestone/books/published/pythonds3/AlgorithmAnalysis/Exercises.html
