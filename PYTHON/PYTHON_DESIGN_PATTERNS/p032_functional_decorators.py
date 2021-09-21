# add additional functionality to object without modifying them or inheriting
# without breaking OCP
# keep functionality separate - single responsibility
# interact with existing structure

import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        stop = time.time()
        print(f"{func.__name__} took {stop-start} seconds")
        return result
    return wrapper


@time_it
def some_op():
    print("starting op")
    time.sleep(1)
    print("done")
    return 123


if __name__ == "__main__":
    # time_it(some_op)()
    some_op()
