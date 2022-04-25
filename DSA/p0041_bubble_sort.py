# def bubble_sort(a_list):
#     for i in range(len(a_list) - 1, 0, -1):
#         for j in range(i):
#             if a_list[j] > a_list[j+1]:
#                 a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(a_list)
# print(a_list)

# short bubble
def bubble_sort_short(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
        if not exchanges:
            break


a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
bubble_sort_short(a_list)
print(a_list)
print(a_list)
