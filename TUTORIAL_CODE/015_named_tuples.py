# subclasses of tuple wih class and field names
# info is stored in class, not instance - hence same memory is consumed
# fields can be accessed by name or position

import collections
Card = collections.namedtuple('Card', {'rank', 'suit'})  # iterable for fields

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')  # single space delimited string for fields
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo.population)
# 36.933
print(tokyo.coordinates)
# (35.689722, 139.691667)
print(tokyo[1])
# 'JP'
print(City._fields)
# ('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
# OR City(*delhi_data)
print(delhi._asdict())
# OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population',
# 21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
for key, value in delhi._asdict().items():
    print(key + ':', value)
# name: Delhi NCR
# country: IN
# population: 21.935
# coordinates: LatLong(lat=28.613889, long=77.208889)
