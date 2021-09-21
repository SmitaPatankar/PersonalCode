lst = [1, 2, 3, 4, 5]

print("O(1)")
print(lst[0])

print("O(logn)")
for index in range(0,len(lst),3):
     print(lst[index])

def f3(n):
    if n <= 0:
        return 1
    else:
        return 1 + f3(n/5)

def f5(n):
    for i in range(0,n,2):
        print(i)  
    if n<=0:
        return 1
    else:
        return 1 + f5(n-5)

print("O(n)")

for element in lst:
     print(element)

def f1(n):
    if n <= 0:
        return 1
    else:
        return 1 + f1(n-1)

def f2(n):
    if n <= 0:
        return 1
    else:
        return 1 + f2(n-5)

print("O(n^2)")
for x in lst:
    for y in lst:
         print(x,y)

print("O(2^n)")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def f4(n,m,o):
    if n<=0:
        print(n,m,o)
    else:
        f4(n-1,m+1,o)
        f4(n-1,m,o+1)

lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [11,12,13,14,15,16,17,18,19] 

print("add complexities")
for a in lst1:
    print(a)
for b in lst2:
    print(b)

print("multiply complexities")
for a in lst1:
    for b in lst2:
        print(a,b)
