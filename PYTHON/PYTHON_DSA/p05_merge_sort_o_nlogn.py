def merge_sort(A):
    if not len(A) > 1:
        return
    mid = len(A)//2
    L = A[:mid]
    R = A[mid:]
    merge_sort(L)
    merge_sort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
    while j < len(R):
        A[k] = R[j]
        j += 1


lst = [10, 5, 20, -1, 0, 100, 2, 1]

print("original---->")
print(lst)

merge_sort(lst)

print("merge sorted---->")
print(lst)
