'''
if you need to store 10 million floating-point values, an array is much more efficient, because an array does not actually hold full-fledged float objects, but only the packed bytes representing their machine values—just like an array in the C language. On the other hand, if you are constantly adding and removing items from the ends of a list as a FIFO or LIFO data structure, a deque (double-ended queue) works faster.
If your code does a lot of containment checks (e.g., item in my_collection), consider using a set for my_collection, especially if it holds a large number of items. Sets are optimized for fast membership checking. But they are not sequences (their content is unordered).
'''


