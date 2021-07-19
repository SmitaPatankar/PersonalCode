def cap(lst):
    if len(lst) == 0:
        return []
    return [str.title(lst[0])] + cap(lst[1:])   

print(cap(["smita", "Neha", "pooja"]))
