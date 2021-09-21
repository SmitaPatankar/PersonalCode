lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # tuple unpacking
print(latitude)
# 33.9425
print(longitude)
# -118.408056

a = 1
b = 2
b, a = a, b

def divmod(x, y):
    return ((x*2, y*2))  # returning as convenient to receiver

print(divmod(20,8))
# (40, 16)

t = (20, 8)

print(divmod(*t))
# (40, 16)

quotient, remainder = divmod(*t)

print(quotient, remainder)
# 40 16

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)
# idrsa.pub
