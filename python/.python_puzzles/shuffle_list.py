import random
def m(lst):
    for i in range(0, len(lst)-1):
        other = random.randint(i, len(lst)-1)
        lst[i], lst[other] = lst[other],lst[i]

l = [0,1,2,3,4,5,6,7,8]
print(l)
m(l)
print(l)
