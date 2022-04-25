def merge_sort(a_list):
    print(f"splitting {a_list}")
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    print(f"merging {a_list}")


l = [100, 1, 5, 10, 2, 9, 3, -1]
print(l)
merge_sort(l)
print(l)

# todo
"""
Recall that the slicing operator is O(k) where k is the size of the slice.
In order to guarantee that merge_sort will be O(nlogn) we will need to remove the slice operator.
Again, this is possible if we simply pass the starting and ending indices along with the list when we
make the recursive call. We leave this as an exercise.
"""
