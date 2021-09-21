def open_russian_doll(n):
    if n == 1:
        return "all dolls are opened"
    print(f"opening doll {n}")
    return open_russian_doll(n-1)

print(open_russian_doll(4))
