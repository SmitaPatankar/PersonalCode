# what is an algorithm?
# ---------------------
# way of solving problem
# in terms of time needed, memory needed, scalability, requirements

"""
linear search
binary search - sorted array - half half
"""

"""
bubble sort - O(n^2) time O(1) memory
quick sort - take an element from start - find element > than that, from end, find element smaller than that, swap them - new start and end - stop when end crosses start and swap end with pivot - repeat for left and right partition
           - last element is pivot - pindex at start - move till find > pivot, if found less than pivot swap
           - O(n^2)
insertion sort - insert at correct position - O(n^2) - too many swaps and comparisons if smaller elements are towards end
merge sort - into 2 arrays and so on - merge them in pairs - O(n log n)`
shell sort - optimized insertion sort - take a gap like 3 - sort - move - reduce gap, reduce gap, gap i.e. insertion sort - O(nlog^2n)
PYTHON list sort uses hybrid merge and insertion
selection sort - find min swap with first, so on for 2nd position - O(n^2)
"""
