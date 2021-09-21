def fib(n):
    assert n >= 0 and int(n) == n, "pass positive integer only"
    if n in [0,1]:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
