from p0011_stack import Stack


def base_converter(decimal_num, base):
    s = Stack()
    digits = "0123456789ABCDEF"
    while decimal_num > 0:
        rem = decimal_num % base
        s.push(rem)
        decimal_num = decimal_num // base
    new_str = ""
    while not s.is_empty():
        new_str += digits[s.pop()]
    return new_str


print(base_converter(25, 2))
print(base_converter(25, 8))
print(base_converter(25, 10))
print(base_converter(25, 16))
