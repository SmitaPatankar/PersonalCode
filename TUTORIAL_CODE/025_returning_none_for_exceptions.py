def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!

# OR


def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


success, result = divide(x, y)
if not success:
    print('Invalid inputs')

_, result = divide(x, y)
if not result:
    print('Invalid inputs')
