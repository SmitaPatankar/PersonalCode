# program: https://www.codingninjas.com/codestudio/problems/reverse-the-array_1262298
# reverse after given position M
# logic: two pointers, swap and move closer, stop both are equal or cross
"""
def reverseArray(arr, m):
    start = m+1  # start = 0 for complete sorting
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return(arr)  # in place sorting, but returned for codestudio
a = [1,2,3,4,5,6]
print(a)
m = 3
print(reverseArray(a, m))
"""

# program: merge sorted arrays in new array
# logic: keep 2 pointers at start of first and 2nd array while both arrays exist, check for <= and add in ans and move
# when one array finishes, other array may still exist, so check for pointer and add remaining elements from leftover array
"""
def merge_sorted_arrays(a, b):
    l = 0
    r = 0
    ans = []
    while l < len(a) and r < len(b):
        if a[l] <= b[r]:
            ans.append(a[l])
            l += 1
        else:
            ans.append(b[r])
            r += 1
    if l < len(a):
        while l < len(a):
            ans.append(a[l])
            l += 1
    elif r < len(b):
        while r < len(b):
            ans.append(b[r])
            r += 1
    return ans
a = [1,3,4,5,7,9]
b = [1,2,6,8,9]
print(a)
print(b)
print(merge_sorted_arrays(a, b))
"""

# hw: program: https://leetcode.com/problems/merge-sorted-array/
# hw: progam: merge 2 sorted arrays in first array that has zeroes in end
# logic: go on filling right empty spaces, thus making left empty spaces
# start comparing elements from end of both arrays for larger element so that we can put it in empty blocks from right side and then left blocks would be empty
"""
def merge(nums1, m, nums2, n):
    # do sorting only until 2nd array is present else, first array is already merge sorted
    while n:
        # if elements in first array exist and righter element in first array is greater > righter element in second array
        if m and nums1[m-1] > nums2[n-1]:
            # put righter element from first array towards the ending open position i.e. m+n-1
            nums1[m+n-1] = nums1[m-1]
            # move first array pointer backwards
            m -= 1  
        # righter element from second array > righter element from first array
        else:
            # put righter element from second array towards the ending open position i.e. m+n-1
            nums1[m + n - 1] = nums2[n-1]  
            # move second array pointer backwards
            n -= 1  
a = [4,5,6,0,0,0]
b = [1,2,3]
print(a)
print(b)
merge(a, 3, b, 3)
print(a)
"""

# program: https://leetcode.com/problems/move-zeroes/
# move zeroes to right
# eg: [0,1,0,3,1,2]
# ans: [1,3,1,2,0,0]
# preserve order
# cant sort as we have to preserve order
# logic keep pointer for place to add non zero value to
# it will begin at 0
# in loop whenever non zero is found, swap with pointer
# move pointer ahead
# if pointer reaches n stop
"""
def move_zeroes(a):
    i = 0
    for j in range(len(a)):
        if a[j] != 0:
            a[i], a[j] = a[j], a[i]
            i += 1
a = [1,0,3,1,0,2]
print(a)
move_zeroes(a)
print(a)
"""
