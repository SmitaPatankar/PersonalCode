from threading import Thread
from queue import Queue

in_queue = Queue()


def consumer():
    print('Consumer waiting')
    work = in_queue.get()      # Done second
    print('Consumer working')
    # Doing work
    # ...
    print('Consumer done')
    in_queue.task_done()       # Done third


Thread(target=consumer).start()
in_queue.put(object())         # Done first
print('Producer waiting')
in_queue.join()                # Done fourth
print('Producer done')

'''
Consumer waitingProducer waiting

Consumer working
Consumer done
Producer done
'''