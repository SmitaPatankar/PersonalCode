import functools

from clockdeco import clock

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__=='__main__':
    print(fibonacci(6))

# $ python3 fibo_demo_lru.py
# [0.00000119s] fibonacci(0) -> 0
# [0.00000119s] fibonacci(1) -> 1
# [0.00010800s] fibonacci(2) -> 1
# [0.00000787s] fibonacci(3) -> 2
# [0.00016093s] fibonacci(4) -> 3
# [0.00001216s] fibonacci(5) -> 5
# [0.00025296s] fibonacci(6) -> 8

# functools.lru_cache(maxsize=128, typed=False)

# decorated function's arguments must be hashable for it
# as lru_cache uses dict to store them

