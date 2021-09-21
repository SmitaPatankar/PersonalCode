# Queue eliminates the busy waiting in the worker by making the get method block until new data is available.

from queue import Queue
from threading import Thread
queue = Queue()


def consumer():
    print('Consumer waiting')
    queue.get()                # Runs after put() below
    print('Consumer done')


thread = Thread(target=consumer)
thread.start()

print('Producer putting')
queue.put(object())
thread.join()
print('Producer done')

# Consumer waiting
# Producer putting
# Consumer done
# Producer done
