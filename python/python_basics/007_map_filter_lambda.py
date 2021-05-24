def times2(i): return i*2

print(times2(5))
# 10

seq = [1, 2, 3, 4, 5]

print(map(times2, seq))
# <map object at 0x03BCFE50>

print(list(map(times2, seq)))
# [2, 4, 6, 8, 10]

print(lambda i: i*2)
# <function <lambda> at 0x05736978>

t = lambda i: i*2
print(t(5))
# 10

print(list(map(lambda i: i*2, seq)))
# [2, 4, 6, 8, 10]

print(filter(lambda i: i % 2 == 0, seq))
# <filter object at 0x0307FEB0>

print(list(filter(lambda i: i % 2 == 0, seq)))
# [2,4]

