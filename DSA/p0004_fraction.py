# fraction algorithm
"""
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    def __eq__(self, other):
        first_num = self.num * other.den 
        second_num = other.num * self.den
        return first_num == second_num  
    def __lt__(self, other):
        first_num = self.num * other.den 
        second_num = other.num * self.den
        return first_num < second_num  
    def __gt__(self, other):
        first_num = self.num * other.den 
        second_num = other.num * self.den
        return first_num > second_num  
f1 = Fraction(1,4)
f2 = Fraction(1,2)
print(f1)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1*f2)
print(f1/f2)
print(f1 == f2)
print(f1<f2)
print(f1>f2)
"""
