def print_exp(tree):
    result = ""
    if tree:
        result = "(" + print_exp(tree.get_left_child())
        result = result + str(tree.get_root_val())
        result = result + print_exp(tree.get_left_child()) + ")"
    return result


# todo
"""
remove brackets
"""
