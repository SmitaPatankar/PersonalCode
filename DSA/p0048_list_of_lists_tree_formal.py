def make_binary_tree(root):
    return [root, [], []]


def insert_left(tree, new_child):
    old_child = tree.pop(1)
    if len(old_child) > 1:
        tree.insert(1, [new_child, old_child, []])
    else:
        tree.insert(1, [new_child, [], []])
    return tree


def insert_right(tree, new_child):
    old_child = tree.pop(2)
    if len(old_child) > 1:
        tree.insert(2, [new_child, [], old_child])
    else:
        tree.insert(2, [new_child, [], []])
    return tree


def get_root_val(tree):
    return tree[0]


def set_root_val(tree, new_value):
    tree[0] = new_value


def get_left_child(tree):
    return tree[1]


def get_right_child(tree):
    return tree[2]


t = make_binary_tree(3)
insert_left(t, 4)
insert_left(t, 5)
insert_right(t, 6)
insert_right(t, 7)
left_child = get_left_child(t)
print(left_child)
set_root_val(left_child, 9)
print(t)
insert_left(left_child, 11)
print(t)
print(get_right_child(get_right_child(t)))

# todo
"""
Write a function build_tree that returns a tree using the list of lists functions that looks like this:
[a, [b, [], [d, [], []]], [c, [e, [], []], [f, [], []]]]
"""
