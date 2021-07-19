# mulitproducer, multiconsumer queues
# FIFO
# LIFO
# priority (sorted and lowest is retrieved first)

# FIFO

# insertion wont work when queue is full

# qsize()
# empty()
# full()
# put()
# get()
# task_done()  # used by consumer after get to show that processing is complete - learn more
# join()  # used until all items are consumed - learn more

import queue as q

myq = q.Queue(maxsize=3)
print(myq.qsize())
print(myq.empty())

myq.put(0)
myq.put(1)
myq.put(2)
print(myq.qsize())
print(myq.full())

print(myq.get())
print(myq.qsize())
