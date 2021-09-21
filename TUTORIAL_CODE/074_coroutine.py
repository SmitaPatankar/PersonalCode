def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


it = my_coroutine()
next(it)             # Prime the coroutine
it.send('First')
it.send('Second')

# Received: First
# Received: Second

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)
it = minimize()
next(it)            # Prime the generator
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))

'''
10
4
4
-1
'''