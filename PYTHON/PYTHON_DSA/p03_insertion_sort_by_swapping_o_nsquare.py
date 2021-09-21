def insertion_sort_by_swapping(a):
    for i in range(1, len(a)):
        for j in range(i-1, -1, -1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            else:
                break


lst = [10, 20, 5, -1, 0, 100, 2]
print("original----->")
print(lst)

insertion_sort_by_swapping(lst)

print("insertion sorted by swapping----->")
print(lst)
