matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = [[x**2 for x in row] for row in matrix]
print(squared)
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
