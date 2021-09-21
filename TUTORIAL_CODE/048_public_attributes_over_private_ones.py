class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


foo = MyObject()
assert foo.public_field == 5

assert foo.get_private_field() == 10

# print(foo.__private_field)
# AttributeError: 'MyObject' object has no attribute '__private_field'


class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field


bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71


class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71


class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field


baz = MyChildObject()
baz.get_private_field()

# AttributeError: 'MyChildObject' object has no attribute '_MyChildObject__private_field'

# The private attribute behavior is implemented with a simple transformation of the attribute name.
# When the Python compiler sees private attribute access in methods like MyChildObject.get_
# private_field, it translates __private_field to access _MyChildObject__private_field instead.
# In this example, __private_field was only defined in MyParentObject.__init__,
# meaning the private attribute’s real name is _MyParentObject__private_field.
# Accessing the parent’s private attribute from the child class fails simply because the
# transformed attribute name doesn’t match.
# Knowing this scheme, you can easily access the private attributes of any class,
# from a subclass or externally, without asking for permission.

assert baz._MyParentObject__private_field == 71
print(baz.__dict__)


# {'_MyParentObject__private_field': 71}

# _ protected
# __ private

class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)


foo = MyClass(5)
assert foo.get_value() == '5'


# above wrong

class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)


foo = MyIntegerSubclass(5)
assert foo.get_value() == 5


class MyBaseClass(object):
    def __init__(self, value):
        self.__value = value
    pass # ...


class MyClass(MyBaseClass):
    pass  # ...

class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)


foo = MyIntegerSubclass(5)
foo.get_value()


# AttributeError: 'MyIntegerSubclass' object has no attribute '_MyClass__value'

class MyClass(object):
    def __init__(self, value):
        # This stores the user-supplied value for the object.
        # It should be coercible to a string. Once assigned for
        # the object it should be treated as immutable.
        self._value = value


# The only time to seriously consider using private
# attributes is when you’re worried about naming conflicts with subclasses.
# This problem occurs when a child class unwittingly defines an
# attribute that was already defined by its parent class.

class ApiClass(object):
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # Conflicts


a = Child()
print(a.get(), 'and', a._value, 'should be different')


# hello and hello should be different

# To reduce the risk of this happening,
# you can use a private attribute in the parent class to
# ensure that there are no attribute names that overlap with child classes.

class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # OK!


a = Child()
print(a.get(), 'and', a._value, 'are different')

# 5 and hello are different
