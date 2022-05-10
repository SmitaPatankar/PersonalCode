# https://drive.google.com/file/d/1FMdN_OCfOI0iAeDlqswCiC2DZzD4nPsb/view

# todo: python: check how multidimensional array works in backend
# todo: python: 2d array program create, input, output, search
# 2d array
"""
eg: for playing x zero

coz we cant handle too many 1d arrays for performing 2d operations

coz we cant handle one big 1 d array for performing 2d operations
[0,  1, 2, 3, 4, 5, 6, 7, 8]
[00,01,02,10,11,12,20,21,22]
r = 3
c = 3
i = 1
j = 2
c*i + j
i.e. 1*3 + 2 = 5

cpp - memory has 1d but visual representation is 2d
"""

# program: 2d array
"""
# create
a = [[None for _ in range(4)] for _ in range(3)]
# input
for r in range(3):
    for c in range(4):
        a[r][c] = int(input(f"enter a[{r}][{c}]"))
    print()
# output
for r in range(3):
    for c in range(4):
        print(a[r][c], end=" ")
    print()
# input column wise
for c in range(4):
    for r in range(3):
        a[r][c] = int(input(f"enter a[{r}][{c}]"))
    print()
# output
for r in range(3):
    for c in range(4):
        print(a[r][c], end=" ")
    print()
# input hardcoded
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# output
for r in range(3):
    for c in range(4):
        print(a[r][c], end=" ")
    print()
# linear search
def is_present(a, n, r, c):
    for i in range(r):
        for j in range(c):
            if a[i][j] == n:
                return True
    return False
print(is_present(a, 5,3,4))
print(is_present(a, 55,3,4))
"""

# program: row wise sum
"""
def row_wise_sum(a, r, c):
    for i in range(r):
        sum = 0
        for j in range(c):
            sum += a[i][j]
        print(f"sum of row number {i} is {sum}")
row_wise_sum([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 3, 4)
"""

# program: column wise sum
"""
def row_wise_sum(a, r, c):
    for j in range(c):
        sum = 0
        for i in range(r):
            sum += a[i][j]
        print(f"sum of col number {j} is {sum}")
row_wise_sum([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 3, 4)
"""

# program: largest row sum
"""
def largest_row_sum(a, r, c):
    largest_row_sum = 0 - 2**31  # int_min
    largest_row_index = -1
    for i in range(r):
        sum = 0
        for j in range(c):
            sum += a[i][j]
        if sum > largest_row_sum:
            largest_row_sum = sum
            largest_row_index = i
    print(f"max sum is of row {largest_row_index} as {largest_row_sum}")
largest_row_sum([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 3, 4)
"""

# program: https://www.codingninjas.com/codestudio/problems/print-like-a-wave_893268
# 2d array of n rows and m columns
# print as sine wave
# first column top to bottom, second column bottom to top, so on
# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# ans: 0 10 20 21 11 1 2 12 22 23 13 3
# logic: for each column, print row element from 0 to r if col num is even, else print r to 0
# logic for odd: number & 1 --> it shows if last bit i.e. bit for 1 is 1 that means odd number
# time complexity is O(nm)
"""
def sine_wave(a, r, c):
    for j in range(c):
        if not j & 1:  # even
            for i in range(r):
                print(a[i][j], end=" ")
        else:  # odd
            for i in range(r-1, -1, -1):
                print(a[i][j], end=" ")
sine_wave([[0,1,2,3],[10,11,12,13],[20,21,22,23]], 3, 4)
"""

# program: https://leetcode.com/problems/spiral-matrix/
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# m rows
# n columns
# 00 01 02 03
# 20 21 22 23
# 30 31 32 33
# 00 01 02 03 23 33 32 32 30 20 21 22
# logic print first row, last col, last row in reverse, first col in reverse, then lower indexing and continue, handle duplicates by update indexing after each print so that it is anyways skipped from everything
# keep tab of printed vs total elements for stopping loop
# O(mn) time complexity
"""
def spiral_print(a):
    rows = len(a)
    cols = len(a[0])
    printed_elements = 0
    total_elements = rows*cols
    starting_row = 0
    ending_row = rows - 1
    starting_column = 0
    ending_column = cols - 1
    ans = []
    while printed_elements < total_elements:
        # print first row
        for col in range(starting_column, ending_column+1):
            if printed_elements < total_elements:
                ans.append(a[starting_row][col])
                printed_elements += 1
        starting_row += 1
        # print last column
        for row in range(starting_row, ending_row+1):
            if printed_elements < total_elements:
                ans.append(a[row][ending_column])
                printed_elements += 1
        ending_column -= 1
        # print last row in reverse
        for col in range(ending_column, starting_column-1, -1):
            if printed_elements < total_elements:
                ans.append(a[ending_row][col])
                printed_elements += 1
        ending_row -= 1
        # print first column in reverse
        for row in range(ending_row, starting_row - 1, -1):
            if printed_elements < total_elements:
                ans.append(a[row][starting_column])
                printed_elements += 1
        starting_column += 1
    return ans
print(spiral_print([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
"""

# todo: check why lo = (n-l)//2
# todo: revise
# hw: program: https://leetcode.com/problems/rotate-image/
# rotate square matrix by 90 degrees
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# logic: look at 4 corners and see how they rotate, keep one as temp and change places of others, put temp back
# once, done move to next corners
# logic: outerloop for denoting no of sides, inner loop for performing transitions as per no of sides
# n=8 l=8 lo=0 hi=7
# n=8 l=6 lo=1 hi=6
# n=8 l=4 lo=2 hi=5
# n=8 l=2 lo=3 hi=4
"""
def print_matrix(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()
def rotate_image(a):
    n = len(a)
    for l in range(n, 1, -2):
        lo = (n-l)//2
        hi = lo + l - 1
        for i in range(l-1):
            temp = a[hi-i][lo]
            a[hi-i][lo] = a[hi][hi-i]
            a[hi][hi-i] = a[lo+i][hi]
            a[lo+i][hi] = a[lo][lo+i]
            a[lo][lo+i] = temp
a = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print_matrix(a)
rotate_image(a)
print()
print_matrix(a)
"""

# todo: math: matrix transformations, reflections, around diagonal etc
# hw: program: https://leetcode.com/problems/rotate-image/
# logic: reverse and transpose - reverse by swapping - transpose like 01 = 10
"""
def print_matrix(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()
def reverse(a):
    n = len(a)
    start = 0
    end = n - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
def transpose(a):
    n = len(a)
    for i in range(n):  # row 0 # row 1 # row 2 # row 3 # row 4
        for j in range(i, n):  # cols 0 1 2 3 4 # cols 1 2 3 4  # cols 2 3 4  # cols 3 4  # cols 4
            a[i][j],a[j][i] = a[j][i],a[i][j]
def rotate(a):
    print_matrix(a)
    print()
    reverse(a)
    print_matrix(a)
    print()
    transpose(a)
    print_matrix(a)
    print()
a = [["00","01","02","03","04"],["10","11","12","13","14"],["20","21","22","23","24"],["30","31","32","33","34"],["40","41","42","43","44"]]
rotate(a)
"""

# program: https://leetcode.com/problems/search-a-2d-matrix/
# program: binary search in 2d array
# count, start, end, mid - as per row and col num
# logic for converting 1d index to 2d, row = n // cols, col = n % cols
# because as many multiples of cols that many rows and remaining cols of current row
# O(log row*col) time complexity
"""
def binary_search_2d(a, n):
    rows = len(a)
    cols = len(a[0])
    count = rows * cols
    start = 0
    end = count - 1
    while start <= end:
        mid = start + (end-start)//2
        mid_row = mid // cols
        mid_col = mid % cols
        mid_element = a[mid_row][mid_col]
        if mid_element == n:
            print(f"{n} found at a[{mid_row}][{mid_col}]")
            return True
        elif mid_element > n:
            end -= 1
        else:
            start += 1
    print(f"{n} not found")
    return False
a = [[1,2,3],[4,5,6],[7,8,9]]
print(binary_search_2d(a, 0))
print(binary_search_2d(a, 3))
print(binary_search_2d(a, 100))
print(binary_search_2d(a, 8))
"""

# todo: revise
# program: https://leetcode.com/problems/search-a-2d-matrix-ii/
# sorted row wise and column wise
# logic: start from first element of last column, if found return, if greater, move forward in same col, if greater, move to previous col
# stop loop when either index goes outside
"""
def search_2d_row_col_wise_sorted(a, n):
    rows = len(a)
    cols = len(a[0])
    count = rows * cols
    row = 0
    col = cols - 1
    while col >= 0 and row < rows:
        our_element = a[row][col]
        if our_element == n:
            print(f"{n} found at a[{row}][{col}]")
            return True
        elif n > our_element:
            row += 1
        else:
            col -= 1
    print(f"{n} not found")
    return False
a = [[1,2,3],[4,5,6],[7,8,9]]
print(search_2d_row_col_wise_sorted(a, 0))
print(search_2d_row_col_wise_sorted(a, 3))
print(search_2d_row_col_wise_sorted(a, 100))
print(search_2d_row_col_wise_sorted(a, 8))
"""

# todo: learn what is n+m time complexity
# hw: program: solve many more 2d array Qs: https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1
# 2d n*m array
# rows are sorted
# find index that has max 1's
# logic: binary search on each row to get starting index of 1 and store it
# next time check rest of them only, so on
"""
def rowWithMax1s(arr, n, m):
    min_first_one_index = m
    ans = -1
    for r in range(n):
        first_one_index = m
        start = 0
        end = min_first_one_index-1
        print(f"binary searching row {r} before index {min_first_one_index}")
        while start <= end:
            mid = start + ((end-start)//2)
            if arr[r][mid] != 1:
                start = mid + 1
            else:
                first_one_index = mid
                end = mid - 1
        if first_one_index < min_first_one_index:
            print(f"so far row {r} has max ones starting from {first_one_index}")
            min_first_one_index = first_one_index
            ans = r
    print()
    print(f"row {ans} has max number of ones starting from {min_first_one_index}")
    return ans
arr = [[0,0,1,1,1],[1,1,1,1,1],[0,1,1,1,1]]
n = 3
m = 5
print(rowWithMax1s(arr,n,m))
"""

# todo: do again later using heap after learning the same
# hw: program: solve many more array Qs: https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1
# square matrix
# rows sorted
# columns sorted
# logic: first element is minimum, last element is maximum, kth smallest element will be between min and max, find mid each time and smart count elements <= mid
# if elements <=mid are less, check ahead, else store ans and check back
# for smart count start from bottom most row's first element, if that is greater than mid, entire row doesnt have, go up
# if <=, all columns up have, save i+1, move to next column
"""
def smart_count_elements_smaller_than_or_eq_to(mat, n, mid):
    row = n - 1
    col = 0
    count = 0
    while row >= 0 and col <= n - 1:
        if mat[row][col] > mid:
            row -= 1
        else:
            count = count + row + 1
            col += 1
    return count
def kthSmallest(mat, n, k):
    low = mat[0][0]
    high = mat[n-1][n-1]
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if smart_count_elements_smaller_than_or_eq_to(mat, n, mid) < k:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans
mat = [[1,2,3],[7,7,8],[11,12,13]]
print(kthSmallest(mat, 3, 5))
"""

# hw: program: solve many more 2d array Qs: https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/
# O(mn) time and one traversal of matrix
# common elements in all rows i.e. elements that occur in each row
# logic keep dict of count of first row elements as 1 avoid duplicate counts by checking count as i before adding
# for next rows, increment if count is i to avoid duplicates else u can ignore as it was anyways not present somewhere above or already added for same row
# on last row, print found elements then and there
# so shift all other columns backwards
# stop when all last elements become same or index reaches 0
"""
def find_common_elements_in_matrix(arr, m, n):
    d = dict()
    for element in arr[0]:
        d[element] = 1
    for r in range(1, m):
        for c in range(0, n):
            element = arr[r][c]
            if element in d.keys() and d[element] == r:
                d[element] += 1
                if r == m-1:
                    print(element)
arr =  [[1, 2, 1, 4, 8],[3, 7, 8, 5, 1],[8, 7, 7, 3, 1],[8, 1, 2, 7, 9]]
m = 4
n = 5
find_common_elements_in_matrix(arr, m, n)
"""

# hw: program: solve many more 2d array Qs: https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
# odd no of elements
# not square matrix
# find median i.e. middle element when sorted
# logic: eg: 1234 5 6789 - median has (length // 2) numbers <= itself and (length//2) numbers >= itself
# search space is given in question
# use binary search to see if our mid is median i.e. had necessary no of elements <= itself
# elements less than or equal to itself can also be found using another binary search on each row as the matrix is sorted row wise
"""
def find_smaller_or_eq_elements(matrix, r, c, n):
    count = 0
    for row in range(r):
        start = 0
        end = c-1
        while start <= end:
            mid = start + ((end-start)//2)
            if matrix[row][mid] <= n:
                start = mid + 1
            else:
                end = mid - 1
        count += start
    return count
def median(matrix, r, c):
    n = (r*c)//2  # no of elements to the left of median including median
    start = 1
    end = 2000
    while start <= end:
        mid = start + ((end-start)//2)
        smaller_or_eq_elements = find_smaller_or_eq_elements(matrix, r, c, mid)
        if smaller_or_eq_elements <= n:
             start = mid + 1
        else:
            end = mid - 1
    return start
matrix = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
r = 3
c = 3
print(median(matrix, r, c))
matrix = [[1],[2],[3]]
r = 3
c = 1
print(median(matrix, r, c))
"""

# todo: solve without using builtin sort and still not getting TLE
# hw: program: solve many more 2d array Qs: https://practice.geeksforgeeks.org/problems/sorted-matrix2333/1
# logic: put in 1d array, sort and put back
"""
def sortedMatrix(N,Mat):
    arr = [0] * N * N
    k = 0
    for i in range(N):
        for j in range(N):
           arr[k] = Mat[i][j]
           k += 1
    arr.sort()
    k = 0
    for i in range(N):
        for j in range(N):
            Mat[i][j] = arr[k]
            k += 1
N = 3
Mat = [[9,1,2],[9,3,4],[1,6,3]]
print(Mat)
sortedMatrix(N, Mat)
print(Mat)
"""

# todo: hw: program: solve many more 2d array Qs: https://practice.geeksforgeeks.org/problems/max-rectangle/1 - after learning dp

# todo: hw: program: solve many more 2d array Qs: https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/ - after learning dp
