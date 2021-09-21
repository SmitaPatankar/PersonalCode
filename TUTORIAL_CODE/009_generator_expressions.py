symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
# brackets not required around genexp
# (36, 162, 163, 165, 8364, 164)

import array
a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)
# array('I', [36, 162, 163, 165, 8364, 164])
# first arg is the storage type
# brackets mandatory around genexp
