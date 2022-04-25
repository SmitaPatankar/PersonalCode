from p0022_dequeue import Deque


def pal_checker(s):
    d = Deque()
    for chr in s:
        d.add_rear(chr)
    while d.size() > 1:
        first = d.remove_front()
        last = d.remove_rear()
        if first != last:
            return False
    return True


print(pal_checker("1221"))
print(pal_checker("121"))
print(pal_checker("1234"))
