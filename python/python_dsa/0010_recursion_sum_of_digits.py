def sumofdigits(num):
    assert num >= 0 and int(num) == num, "pass positive integer only"
    if num == 0:
        return 0
    return (num % 10) + sumofdigits(num // 10)

print(sumofdigits(12378))
