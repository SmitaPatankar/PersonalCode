# create
newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple)

newTuple1 = tuple('abcde')
print(newTuple1)

myTuple = (1,4,3,2,5)
print(newTuple1)

myTuple1 = (1,2,6,9,8,7)
print(newTuple1)

# access
print(newTuple[0]) 

# traverse
for i in newTuple:
    print(i)

for index in range(len(newTuple)):
    print(newTuple[index])

# search
print('a' in newTuple)

for i in newTuple:
    if i == "a":
        print(newTuple.index(i))

# extend and create new
print(myTuple + myTuple1) 

# repeat and create new
print(myTuple * 4)      

# count
myTuple1.count(2)

# index
myTuple1.index(2)
