def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division(1, 10 ** 500, True, False)
print(result)  # 0.0

result = safe_division(1, 0, False, True)
print(result)  # inf

def safe_division_b(number, divisor,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division_b(1, 10 ** 500, ignore_overflow=True)
safe_division_b(1, 0, ignore_zero_division=True)

safe_division_b(1, 10 ** 500, True, False)


def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# after * kw only args

# safe_division_c(1, 10 ** 500, True, False)
# TypeError: safe_division_c() takes 2 positional arguments but 4 were given


safe_division_c(1, 0, ignore_zero_division=True)  # OK

try:
    safe_division_c(1, 0)
except ZeroDivisionError:
    pass  # Expected
