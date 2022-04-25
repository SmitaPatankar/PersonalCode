def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)


def partition(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark += 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
    return right_mark


l = [100, 2, -1, 3, 1, 5, 0, 0, 8]
print(l)
quick_sort(l)
print(l)

# todo
"""
In particular, we can attempt to alleviate some of the potential for an uneven division by using a
technique called median of three. To choose the pivot value, we will consider the first, the middle,
and the last element in the list. In our example, those are 54, 77, and 20. Now pick the median value,
in our case 54, and use it for the pivot value (of course, that was the pivot value we used originally).
The idea is that in the case where the first item in the list does not belong toward the middle of the list,
the median of three will choose a better “middle” value. This will be particularly useful when the original
list is somewhat sorted to begin with.
We leave the implementation of this pivot value selection as an exercise.

https://runestone.academy/runestone/books/published/pythonds3/SortSearch/DiscussionQuestions.html

https://runestone.academy/runestone/books/published/pythonds3/SortSearch/Exercises.html
"""
