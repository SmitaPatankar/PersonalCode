from p0019_queue import Queue


def hot_potato(name_list, num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num - 1):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


print(hot_potato([str(x) for x in range(1, 40)], 7))
