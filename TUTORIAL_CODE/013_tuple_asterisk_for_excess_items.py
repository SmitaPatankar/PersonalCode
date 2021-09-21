a, b, *rest = range(5)
print(a, b, rest)
# 0 1 [2, 3, 4]
a, b, *rest = range(3)
print(a, b, rest)
# 0 1 [2]
a, b, *rest = range(2)
print(a, b, rest)
# 0 1 []
a, *body, c, d = range(5)
print(a, body, c, d)
# 0 [1, 2] 3 4
*head, b, c, d = range(5)
print(head, b, c, d)
# [0, 1] 2 3 4
