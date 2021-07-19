d =  [4,5,6,7,2,3,11,13]
l = 0
r = len(d) - 1
while l < r:
    while d[l] % 2 == 0 and l <r:
        l += 1
    while d[r] %2 != 0 and l<r:
        r -= 1
    if l < r:
        d[l], d[r] = d[r], d[l]
print(d)