# sequence of values
# any type
# indexed
# immutable
# hashable - value remains same during lifetime
# in adjacent locations in memory

# create
# time = O(1)
# space = O(n)
t = (1,2)
print(t)
t = 1,2
print(t)
t = (1,)
print(t)
t = 1,
print(t)
t = ()
print(t)
t = tuple()
print(t)
t = tuple('abcde')  # separates
print(t)

# access
# time - O(1)
# space - O(1)
print(t[0])
print(t[-1])

# access - slicing
# time - O(1)
# space - O(1)
print(t[0:2])
print(t[:2])
print(t[2:])
print(t[:])

# traverse
# time - O(n)
# space - O(1)
for i in t:
    print(i)
for i in range(len(t)):
    print(t[i])

# search - with in
# time - O(n)
# space - O(1)
print("b" in t)

# search - linear
# time - O(n)
# space - O(1)
for i in t:
    if i == "b":
        print(t.index(i))
