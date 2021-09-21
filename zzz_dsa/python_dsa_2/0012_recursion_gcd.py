# numbers are 48, 18
# 48%18=12
# 18%12=6
# 12%6=0   
# 6%0 --> stop --> gcd is 6

def gcd(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, "integer only"
    if n1 < 0:
        n1 = -1 * n1
    if n2 < 0:
        n2 = -1 * n2
    if n2 == 0:
        return n1
    return gcd(n2, n1%n2)

print(gcd(48, 18))
