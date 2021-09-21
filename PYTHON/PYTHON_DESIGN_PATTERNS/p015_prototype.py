# copy object and make use

import copy


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.address}"


class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.country = country
        self.street_address = street_address

    def __str__(self):
        return f"{self.city} - {self.street_address} - {self.country}"


p = Person("smita", Address("nehru road", "mumbai", "india"))

j = copy.deepcopy(p)
j.name = "john"

print(p)
print(j)
