from p0011_stack import Stack


def divide_by_2(dec):
    s = Stack()
    while dec > 0:
        rem = dec % 2
        s.push(rem)
        dec = dec // 2
    bin = ""
    while not s.is_empty():
        bin += str(s.pop())
    return bin


print(divide_by_2(32))
print(divide_by_2(33))
