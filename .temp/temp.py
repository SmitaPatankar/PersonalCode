def reverse_number(n):
    if n == 0:
        return n
    digit = n % 10
    print(f"digit is {digit}")
    new_n = n//10
    print(f"consolidated number is {(digit * 10) + reverse_number(new_n)}")
    return  (digit*10) + reverse_number(new_n)

print(reverse_number(12345))
# 54321


# 12345
# digit  5 4 3 2 1
# number 1234 123 12 1 0