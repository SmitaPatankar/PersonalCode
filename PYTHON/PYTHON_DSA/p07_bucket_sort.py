from functools import reduce


def bucket_sorted(lst):
    max_digits = get_max_digits(lst)
    for digit_index in range(0, max_digits):
        bucket = [[] for _ in range(10)]
        for item in lst:
            digit_value = get_digit_at_index(item, digit_index)
            bucket[digit_value].append(item)
        lst = flatten(bucket)
    return lst


def get_max_digits(lst):
    max_item = lst[0]
    for item in lst:
        if item > max_item:
            max_item = item
    return len(str(max_item))


def get_digit_at_index(item, index):
    return item // 10 ** (index) % 10


def flatten(lst):
    return reduce(lambda x, y: x+y, lst)


my_lst = [10, 5, 20, 1579, 0, 10, 2]
print("original----->")
print(my_lst)

print("bucket sorted----->")
print(bucket_sorted(my_lst))
