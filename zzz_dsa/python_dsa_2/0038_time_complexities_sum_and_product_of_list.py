def foo(lst):
    sum = 0
    product = 1
    for i in lst:
        sum += i
    for i in lst:
        product *= i
    return("Sum = "+str(sum)+", Product = "+str(product))

print(foo([1,2,3,4]))

# O(n)
