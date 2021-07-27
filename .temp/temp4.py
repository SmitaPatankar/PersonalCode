# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(10))
# # 0 1 1 2 3 5 8 13 21 34

def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        result = [0,1]
    for _ in range(2,n):
        result.append(result[-1] + result[-2])
    return result

print(fib(10))
# 0 1 1 2 3 5 8 13 21 34

# xpath
# table
# th
# tr
# td

# new wait
# fluent wait

# jscript
# scroll

# test plan
