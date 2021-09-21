# create
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList)

myList = [1,2,3,4,5,6,7]
print(myList)

# traverse
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])

# insert
myList.insert(4,15)

# append
myList.append(55)

# extend
newList = [11,12,13,14]
myList.extend(newList)
print(myList)

# search
for i in list:
    if i == 5:
        print("found")
