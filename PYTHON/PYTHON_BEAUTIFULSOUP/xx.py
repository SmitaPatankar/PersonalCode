# import re
# s = "this   is   a string"
# print(" ".join(re.findall("\w+", s)))

s = "this   is   a string"
new_s = ""
for i in range(len(s)):
    if not (s[i] == " " and s[i+1] == " "):
        new_s += s[i]
print(new_s)
