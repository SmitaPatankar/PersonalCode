def poweroftwo(n):
    product = 1
    i = 0
    while i < n:
        product = product * 2
        i += 1
    return product

print(poweroftwo(8))
