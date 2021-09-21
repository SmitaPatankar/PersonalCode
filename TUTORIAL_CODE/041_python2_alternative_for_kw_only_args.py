def print_args(*args, **kwargs):
    print('Positional:', args)
    print('Keyword:   ', kwargs)


print_args(1, 2, foo='bar', stuff='meep')

'''
Positional: (1, 2)
Keyword:    {'foo': 'bar', 'stuff': 'meep'}
'''


def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_div:
            return float('inf')
        else:
            raise


safe_division_d(1, 10)
safe_division_d(1, 0, ignore_zero_division=True)
safe_division_d(1, 10 ** 500, ignore_overflow=True)

safe_division_d(1, 0, False, True)
# TypeError: safe_division_d() takes 2 positional arguments but 4 were given

safe_division_d(0, 0, unexpected=True)
# TypeError: Unexpected **kwargs: {'unexpected': True}
