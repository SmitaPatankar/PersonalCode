from p0011_stack import Stack


def revstring(mystr):
    s = Stack()
    for c in mystr:
        s.push(c)
    revstr = ""
    while not s.is_empty():
        revstr += s.pop()
    return revstr


print(revstring("smita"))
