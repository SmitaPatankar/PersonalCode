# concatenate
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)

# repeat
print(a*5)

# count no of elements
print(len(a))

# max
print(max(a))

# min
print(min(a))

# sum
print(sum(a))

# average
print(sum(a)/len(a))

# average
# p = []
# while True:
#     s = input("enter a number")
#     if s == "done":
#         break
#     p.append(float(s))
# print(sum(p)/len(p))

# list of chars from string
s = "smita neha"
print(list(s))

# list of words from string
s = "smita neha"
print(s.split())
s = "smita,neha"
print(s.split(","))

# string from list
l = ["ab", "cd"]
print(",".join(l))

# sort in place
l.sort()
print(l)

# sort and return new list
print(sorted(l))
