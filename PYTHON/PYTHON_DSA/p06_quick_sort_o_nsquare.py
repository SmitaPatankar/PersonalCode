def quick_sort(a):
    quick_sort_internal(a, 0, len(a)-1)


def quick_sort_internal(a, start, end):
    if start < end:
        sorted_pivot_index = get_sorted_pivot_index(a, start, end)
        quick_sort_internal(a, start, sorted_pivot_index - 1)
        quick_sort_internal(a, sorted_pivot_index + 1, end)


def get_sorted_pivot_index(a, start, end):
    pivot_index = get_pivot_index(a, start, end)
    pivot_value = a[pivot_index]
    a[start], a[pivot_index] = a[pivot_index], a[start]
    border = start
    for i in range(start, end+1):
        if a[i] < pivot_value:
            border += 1
            a[i], a[border] = a[border], a[i]
    a[start], a[border] = a[border], a[start]
    return border


def get_pivot_index(a, start, end):
    mid = (start + end)//2
    pivot_value = sorted([start, mid, end])[1]
    if a[start] == pivot_value:
        return start
    elif a[mid] == pivot_value:
        return mid
    else:
        return end


lst = [10, 5, 20, -1, 0, 100, 2]

print("original---->")
print(lst)

quick_sort(lst)

print("quick sorted---->")
print(lst)
