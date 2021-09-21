def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', [1, 2])
log('Hi there', [])

'''
My numbers are: 1, 2
Hi there
'''


def log(message, *values):  # The only difference
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', 1, 2)
log('Hi there')  # Much better

'''
My numbers are: 1, 2
Hi there
'''

favorites = [7, 33, 99]
log('Favorite colors', *favorites)

# Favorite colors: 7, 33, 99


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))

log(1, 'Favorites', 7, 33)      # New usage is OK
log('Favorite numbers', 7, 33)  # Old usage breaks

'''
1: Favorites: 7, 33
Favorite numbers: 7: 33
'''
