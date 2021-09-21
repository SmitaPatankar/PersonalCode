#       32 16 8 4 2 1
# 14 =        1 1 1 0

# decimal is 15
# 14%2=0 14//2=7
# 7%2=1  7//2=3
# 3%2=1  3//2=1
# 1%2=1  1//2=0
# 0%2 --> stop --> binary is 1110

def dectobin(dec):
    if dec == 0:
        return 0
    return (dec%2) + (10 * dectobin(dec//2))

print(dectobin(14))
