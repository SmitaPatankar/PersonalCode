# def bestscores(lst):
#     first = 0
#     second = 0
#     for element in lst:
#         if element > first:
#             second = first
#             first = element
#         elif element > second:
#             second = element
#     return first, second

# print(bestscores([100,90,80,70]))

def firstSecond(given_list):
    a = given_list 
    a.sort(reverse=True)
    first = a[0]
    second = None 
    for element in given_list:
        if element != first: 
            second = element
            return first, second

print(firstSecond([100,90,80,70]))
