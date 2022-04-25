def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(a_list, pos_start, sublist_count)
        print(f"after increment of size {sublist_count} the list is {a_list}")
        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val


l = [1000, 8, 5, 0, 1, 2, 3, -1, 6, 100]
print(l)
shell_sort(l)
print(l)
