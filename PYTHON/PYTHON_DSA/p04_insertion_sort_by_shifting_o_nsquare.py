def insertion_sort_by_shifting(a):
    for i in range(1, len(a)):
        curnum = a[i]
        j = i-1
        while j >= 0 and a[j] > curnum:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = curnum


lst = [10, 20, 5, -1, 0, 100, 2]
print("original----->")
print(lst)

insertion_sort_by_shifting(lst)

print("insertion sorted by shifting----->")
print(lst)
