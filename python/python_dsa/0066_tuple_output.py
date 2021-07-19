init_tuple = ()
print (init_tuple.__len__())
# 0 

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print(init_tuple_a == init_tuple_b)
# True 

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print (init_tuple_a + init_tuple_b)
# (1, 2, 3, 4)
 
init_tuple_a = 1, 2
init_tuple_b = (3, 4)
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]
# 10

init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)
print(result)
# 6

l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)
# ()
 
init_tuple = ('Python') * 3
print(type(init_tuple))
# <class ‘str’>

# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)
# TypeError: ‘tuple’ object does not support item assignment

init_tuple = ((1, 2),) * 7
print(init_tuple)
print(len(init_tuple[3:10]))
# 4
