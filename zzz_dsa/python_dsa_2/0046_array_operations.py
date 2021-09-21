from array import array

# create
my_array = array('i',[1,2,3,4,5])

# traverse
for i in my_array:
    print(i)

# access
print(my_array[3])

# append
my_array.append(6)
print(my_array)

# insert
my_array.insert(3, 11)
print(my_array)

# extend
my_temp_array = array('i', [10,11,12])
my_array.extend(my_temp_array)
print(my_array)

# add from list
my_temp_list = [20,21,22]
my_array.fromlist(my_temp_list)
print(my_array)

# remove
my_array.remove(11)
print(my_array)

# pop
print(my_array.pop())
print(my_array)

# index
print(my_array.index(21))

# reverse
my_array.reverse()
print(my_array)

# buffer info
print(my_array.buffer_info())

# count
print(my_array.count(21))

# slice
print(my_array[:])

# to list
print(my_array.tolist())
