def bubble_sort(a):
    for i in range(0, len(a)-1):
        done = True
        for j in range(0, len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                done = False
        if done:
            return


lst = [10, 20, 5, -1, 0, 100, 2]
print("original---->")
print(lst)

bubble_sort(lst)

print("bubble sorted----->")
print(lst)
