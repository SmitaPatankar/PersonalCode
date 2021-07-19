# find missing element in array
# -----------------------------
# sum of all numbers should ideally be n(n+1)/2
# missing number will be the difference between actual sum and ideal sum

# find all pairs of integers from array whose sum is equal to given number
# ------------------------------------------------------------------------
# does it contain negative numbers?
# do we need to print repeat pairs?
# do we need to print reverse pairs?
# do both elements of pair need to be unique? Y
# how big is the array?
# ---------------------
# loop over array and inside that loop over array ahead of current index in outer loop
# skip if both elements in pair are same

# find number in array
# ---------------------
# find linearly

# max product of 2 integers in array where all elements are positive
# -------------------------------------------------------------------
# loop over array and internally loop over array ahead of current index from outer loop

# list is unique / has duplicates
# -------------------------------
# make a blank visited list, visit each element in array, check if it exists in visited list and add it to visited list
# if it already exists, that means unique is false

# check if one list is permutation of other
# -----------------------------------------
# check if lengths match
# if yes, check if sorted lists match

# rotate matrix by 90 degrees
# ---------------------------
# 1 2 3
# 4 5 6
# 7 8 9
# 
# 7 4 1
# 8 5 2
# 9 6 3
# 
# loop over layers i.e. squares
#     loop over one one element from each side
#         save first element
#         move 2nd to first
#         move third to second
#         move fourth to third
#         move first saved one to fourth
# ---------------------------------------
import numpy as np
def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]
            matrix[i][- layer - 1] = top
    return matrix
matrix = np.array([[1,2], [3,4]])
print(matrix)
print(rotate_matrix(matrix))

# sum of diagonal elements of 2d matrix
# -------------------------------------
# loop over the length of matrix using say i and add a[i][i]

# first and second best score from list with duplicates
# -----------------------------------------------------
# reverse sort the list
# max will be first element
# second max will be received by looping over the list when element is not equal to max

# remove duplicates from list
# ---------------------------
# create empty list
# loop over actual list and add to new list if element doesnt exist there already
