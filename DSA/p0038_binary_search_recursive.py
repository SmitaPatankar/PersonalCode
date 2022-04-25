def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint + 1 :], item)


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_rec(test_list, 3))
print(binary_search_rec(test_list, 13))

# todo
"""
Slice operator in Python is actually O(k). 
This means that the binary search using slice will not perform in strict logarithmic time. 
Luckily this can be remedied by passing the list along with the starting and ending indices. 
The indices can be calculated as we did earlier.
"""
