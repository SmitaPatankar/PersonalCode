l = [5,4,3,2]
for i in range(len(l) - 1):
    a = 0
    b = 1
    while b < len(l) - i:
        print(a)
        print(b)
        print("---")
        if l[a] > l[b]:
            l[a], l[b] = l[b], l[a]
            a += 1
            b += 1
print(l)