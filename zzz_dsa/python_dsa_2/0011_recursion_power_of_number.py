def powerofnum(num, pow):
    if pow == 0:
        return 1
    return num * powerofnum(num, pow - 1)

print(powerofnum(5, 3))
