def function(n):
    if n < 1:
        return("n < 1")
    print(n)
    return function(n-1)

print(function(5))
