def cap(lst):
    result = []
    if len(lst) == 0:
        return result
    result.append(lst[0].upper())
    return result + cap(lst[1:])

print(cap(["Smita", "neha", "PRIYANKA"]))
