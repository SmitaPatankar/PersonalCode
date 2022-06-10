# program - recursion - give reverse of string - https://www.codingninjas.com/codestudio/problems/reverse-the-string_799927
"""
def reverse_string(s, start, end):
    if start >= end:
        return "".join(s)
    s = list(s)
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1
    return reverse_string(s, start, end)
print(reverse_string("", start=0, end=0))
print(reverse_string("s", start=0, end=0))
print(reverse_string("smita", start=0, end=4))
"""

# hw: program: recursion: reverse string with one pointer only for calculating start and end
"""
def reverse_string(s, start):
    end = len(s) - start - 1
    if start >= end:
        return "".join(s)
    s = list(s)
    s[start], s[end] = s[end], s[start]
    start += 1
    return reverse_string(s, start)
print(reverse_string("", start=0))
print(reverse_string("s", start=0))
print(reverse_string("smita", start=0))
"""

# program - recursion - check if palindrome - https://www.codingninjas.com/codestudio/problems/check-palindrome_920555
# hw: program: recursion: check if palindrome: use only one pointer for start and end
"""
def check_palindrome(s, start=0):
    s = list(s)
    end = len(s) - start - 1
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    else:
        start += 1
        return check_palindrome(s, start)
print(check_palindrome(""))
print(check_palindrome("s"))
print(check_palindrome("abcba"))
print(check_palindrome("abccba"))
print(check_palindrome("smita"))
"""

# program - recursion - return a^b
# logic - 2^8 = 2^4 * 2^4 - 2^4 = 2^2 * 2^2 - 2^2 = 2^1 * 2^1 - 2^1 = 2^0 * 2 ^ 0 i.e. 1
# logic = 2 ^ 9 = 2 * 2^4 * 2^4 and so on...
# complexity - 1024 - 512 - 256 - 128 - 64 - 32 - 16 - 8 - 4 - 2 - 1 - 0 --> instead of 1024 iterations we took 10 iterations
"""
def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    ans = power(a, b // 2)
    if b % 2 == 0:
        return ans * ans
    else:
        return a * ans * ans
print(power(2,0))
print(power(2,1))
print(power(2,5))
print(power(2,6))
"""

# program - bubble sort - recursion
"""
def bubble_sort(arr, n):
    print(f"{arr}")
    if n == 1 or n == 0:
        return True
    sorted = True
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            sorted = False
            arr[i], arr[i+1] = arr[i+1], arr[i]
    if sorted:
        return
    else:
        bubble_sort(arr, n-1)
arr = [5,4,6,1,2,3]
bubble_sort(arr, 6)
print(arr)
"""

# hw: selection sort - recursion
"""
def selection_sort(arr, n, index=0):
    if n == 1:
        return
    min_value = arr[index]
    min_index = index
    for i in range(index+1, index+n):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
    if index != min_index:
        arr[index], arr[min_index] = arr[min_index], arr[index]
    print(arr)
    selection_sort(arr, n-1, index+1)
arr = [5,4,6,1,2,3]
print(arr)
selection_sort(arr, 6)
print(arr)
"""

# hw: insertion sort - recursion
"""
def insertion_sort(arr, current_index=1):
    print(f"current_index {current_index}")
    if current_index == len(arr):
        return
    temp = arr[current_index]
    i = current_index - 1
    while i >= 0:
        if temp < arr[i]:
            arr[i+1] = arr[i]
            i -= 1
        else:
            break
    arr[i+1] = temp
    print(arr)
    insertion_sort(arr, current_index+1)
arr = [5,4,6,1,2,3]
print(arr)
insertion_sort(arr)
print(arr)
"""
