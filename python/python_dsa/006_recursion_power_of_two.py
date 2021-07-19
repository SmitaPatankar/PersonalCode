def poweroftwo(n):
    if n == 0:
        return 1
    return 2 * poweroftwo(n-1)

print(poweroftwo(8))
