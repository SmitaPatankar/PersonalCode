from time import time
import select


def slow_systemcall():
    select.select([], [], [], 0.1)


start = time()
for _ in range(5):
    slow_systemcall()
end = time()
print('Took %.3f seconds' % (end - start))
# Took 0.503 seconds