# can be processed in parallel by multiple concurrent workers

# learn more

from multiprocessing import Queue

q = Queue(maxsize=3)

q.put(0)
q.put(1)
q.put(2)

print(q.get())
