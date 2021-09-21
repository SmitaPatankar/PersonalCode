###########################imports###########################

import functools

###########################defining a function###########################

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

###########################replacing one function with other - information lost###########################

def f(x):
    """square"""
    return x*x

f = logged(f)
print(f(5))
# f was called
# 25

print(f.__name__)  # with_logging

###########################using one function as decorator for other - information lost###########################

@logged
def f(x):
    """square"""
    return x*x


print(f(5))
# f was called
# 25

print(f.__name__)  # with_logging

############using one function as decorator for other function, but wrapping it with main function's info###############

def logged(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    """square"""
    return x*x

print(f(10))
# f was called
# 100

print(f.__name__)
# f
