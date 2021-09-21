def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1  # immutable local var
        total += new_value
        return total / count

    return averager

avg = make_averager()
avg(10)
# Traceback (most recent call last):
#   ...
# UnboundLocalError: local variable 'count' referenced before assignment

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

