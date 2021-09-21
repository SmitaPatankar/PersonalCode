from threading import Thread
from queue import Queue
import time

queue = Queue(1)               # Buffer size of 1


def consumer():
    time.sleep(0.1)            # Wait
    queue.get()                # Runs second
    print('Consumer got 1')
    queue.get()                # Runs fourth
    print('Consumer got 2')


thread = Thread(target=consumer)
thread.start()

queue.put(object())            # Runs first
print('Producer put 1')
queue.put(object())            # Runs third
print('Producer put 2')
thread.join()
print('Producer done')

'''
Producer put 1
Consumer got 1Producer put 2
Consumer got 2

Producer done
'''