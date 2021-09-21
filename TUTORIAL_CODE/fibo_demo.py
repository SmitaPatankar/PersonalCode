from clockdeco import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))

# python3 fibo_demo.py
# [0.00000095s] fibonacci(0) -> 0
# [0.00000095s] fibonacci(1) -> 1
# [0.00007892s] fibonacci(2) -> 1
# [0.00000095s] fibonacci(1) -> 1
# [0.00000095s] fibonacci(0) -> 0
# [0.00000095s] fibonacci(1) -> 1
# [0.00003815s] fibonacci(2) -> 1
# [0.00007391s] fibonacci(3) -> 2
# [0.00018883s] fibonacci(4) -> 3
# [0.00000000s] fibonacci(1) -> 1
# [0.00000095s] fibonacci(0) -> 0
# [0.00000119s] fibonacci(1) -> 1
# [0.00004911s] fibonacci(2) -> 1
# [0.00009704s] fibonacci(3) -> 2
# [0.00000000s] fibonacci(0) -> 0
# [0.00000000s] fibonacci(1) -> 1
# [0.00002694s] fibonacci(2) -> 1
# [0.00000095s] fibonacci(1) -> 1
# [0.00000095s] fibonacci(0) -> 0
# [0.00000095s] fibonacci(1) -> 1
# [0.00005102s] fibonacci(2) -> 1
# [0.00008917s] fibonacci(3) -> 2
# [0.00015593s] fibonacci(4) -> 3
# [0.00029993s] fibonacci(5) -> 5
# [0.00052810s] fibonacci(6) -> 8
# 8
