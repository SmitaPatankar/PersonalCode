x = [1,2,3,4]

# normal
out = []
for i in x:
    out.append(i**2)
print(out)
# [1, 4, 9, 16]

# list comprehension
out = [i**2 for i in x]
print(out)
# [1, 4, 9, 16]
