import json
handle = open('023_better_than_022_avoiding_else_with_for_and_while.py')  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()  # Always runs after try:


def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]  # May raise KeyError


# all

UNDEFINED = object()


def divide_json(path):
    handle = open(path, 'r+')  # May raise IOError
    try:
        data = handle.read()  # May raise UnicodeDecodeError
        op = json.loads(data)  # May raise ValueError
        value = (
                op['numerator'] /
                op['denominator'])  # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)  # May raise IOError
        return value
    finally:
        handle.close()  # Always runs
