def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursive_factorial(n-1)


print(get_recursive_factorial(5))

# requires memory as lot of calls get opened up until we reach the last call
# iterative solutions may be faster in some languages
# may be harder to understand than iterative

# in some cases it is fast and easy eg: tree traversals and binary searches