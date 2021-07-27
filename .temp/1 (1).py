# fibonacci series
# user will give length

# def fibonacci(length):
#     if length < 1:
#         return []
#     if length == 1:
#         return [0]
#     if length == 2:
#         return [0,1]
#     output = [0,1]
#     for _ in range(length-2):
#         output.append(output[-1] + output[-2])
#     return output

# print(fibonacci(10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# def fibonacci(length, output=[]):
#     if length == 1:
#         output.append(0)
#     elif length == 2:
#         output.append(2)
#     else:

#     fibonacci(length,output)
#     length = length - 1
# print(fibonacci(10))


# def _fib(index):
#     if index in [0,1]:
#         return index
#     return _fib(index-1) + _fib(index-2)
# def fibonacci(length):
#     for i in range(length):
#         print(_fib(i), end = " ")

# fibonacci(10)
