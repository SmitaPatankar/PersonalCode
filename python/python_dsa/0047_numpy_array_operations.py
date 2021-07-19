import numpy as np

# create
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# insert
newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)

# length
print(len(twoDArray))

# append
newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)

# access
print(twoDArray[0][0])

# traverse
for i in range(len(twoDArray)):
    for j in range(len(twoDArray[0])):
        print(twoDArray[i][j])

# search
for i in range(len(twoDArray)):
    for j in range(len(twoDArray[0])):
        if twoDArray[i][j] == 444:
            print("found")
            break

# delete
newTwoDArray = np.delete(twoDArray, 1, axis=1)
print(newTwoDArray)
