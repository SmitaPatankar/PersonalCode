# copy object and make use

import copy


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.address}"


class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.suite = country
        self.street_address = street_address

    def __str__(self):
        return f"{self.city} - {self.street_address} - {self.suite}"


class EmployeeFactory:
    main_ofc_employee = Employee("", Address("bellandur", "bangalore", 0))
    aux_ofc_employee = Employee("", Address("bellandur", "bangalore", 0))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_ofc_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_ofc_employee, name, suite)

    @staticmethod
    def new_aux_ofc_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_ofc_employee, name, suite)


john = EmployeeFactory.new_main_ofc_employee("john", "1")
matt = EmployeeFactory.new_aux_ofc_employee("matt", "2")

print(john)
print(matt)
