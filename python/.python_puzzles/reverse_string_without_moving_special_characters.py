"""
Input string:  a!!!b.c.d,e'f,ghi
Output string:  i!!!h.g.f,e'd,cba
"""
s = "a!!!b.c.d,e'f,ghi"
print(s)
s = list(s)
l = 0
r = len(s) - 1
while l < r:
    if s[l].isalpha() and s[r].isalpha():
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    else:
        if not s[l].isalpha():
            l += 1
        if not s[r].isalpha():
            r -= 1

print("".join(s))
