# Python 2
x = 'my precious'
dummy = [x for x in 'ABC']
print(x)
'C'

#  Python 3
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
'ABC'
print(dummy)
# [65, 66, 67]
