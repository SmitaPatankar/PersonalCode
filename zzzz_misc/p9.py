# input
l1 = ["a", "b", "c", "d"]
l2 = ["e", "f", "g", "h"]

# expected output
# l3 = ["ae", "bf", "cg", "dh"]

# zip
z = dict(zip(l1, l2))
l = [f"{k}{v}" for k,v in z.items()]
print(l)

# iteration
l3 = []
for i in range(len(l1)):
    l3.append(f"{l1[i]}{l2[i]}")
print(l3)

# comprehension
l3 = [f"{l1[i]}{l2[i]}" for i in range(len(l1))]
print(l3)
