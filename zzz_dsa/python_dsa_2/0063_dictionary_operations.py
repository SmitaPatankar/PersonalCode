# create
myDict = {'name': 'Edy', 'age': 26}
print(myDict)

# update
myDict['address'] = 'London'
print(myDict)

# traverse
for key in myDict:
    print(key, myDict[key])

# search
for key in myDict:
    if myDict[key] == 27:
        print(key)

# pop
myDict.pop('name')

# sort into list of keys
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
print(sorted(myDict, key=len))
