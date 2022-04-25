def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos -= 1
        a_list[cur_pos] = cur_val


l = [100, -1, 0, 5, 3, 2, 10]
print(l)
insertion_sort(l)
print(l)
