from time import time
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]
start = time()
results = list(map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))


###############################################
from concurrent.futures import ThreadPoolExecutor
start = time()
pool = ThreadPoolExecutor(max_workers=2)
_ = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))

# Took 1.199 seconds
# It’s even slower this time because of the overhead of starting and communicating with the pool of threads.

#################################################
from concurrent.futures import ProcessPoolExecutor
start = time()
pool = ProcessPoolExecutor(max_workers=2)  # The one change
_ = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))

# Took 0.663 seconds

'''
1. It takes each item from the numbers input data to map.

2. It serializes it into binary data using the pickle module (see Item 44: “Make pickle Reliable with copyreg”).

3. It copies the serialized data from the main interpreter process to a child interpreter process over a local socket.

4. Next, it deserializes the data back into Python objects using pickle in the child process.

5. It then imports the Python module containing the gcd function.

6. It runs the function on the input data in parallel with other child processes.

7. It serializes the result back into bytes.

8. It copies those bytes back through the socket.

9. It deserializes the bytes back into Python objects in the parent process.

10. Finally, it merges the results from multiple children into a single list to return.
'''

