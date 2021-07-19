def f(lst):
    palindromes = []
    for n in lst:
        reverse = 0
        tens = 1
        temp = n
        while n % 10 > 0:
            digit = n % 10
            n = n // 10
            reverse = (tens * reverse) + digit
            tens = 10
        if reverse == temp:
            palindromes.append(temp)
    return palindromes

print(f([1,12,121,125,525,646,17,22,2,0]))
