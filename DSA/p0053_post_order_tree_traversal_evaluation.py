import operator


def postordereval(tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result_1 = None
    result_2 = None
    if tree:
        result_1 = postordereval(tree.get_left_child())
        result_2 = postordereval(tree.get_right_child())
        if result_1 and result_2:
            return operators[tree.get_root_val()](result_1, result_2)
        else:
            return tree.get_root_val()
