# If your class defines __getattr__, that method is called every time an
# attribute can’t be found in an object’s instance dictionary.

class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

data = LazyDB()

data = LazyDB()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After: ', data.__dict__)

'''
Before: {'exists': 5}
foo:    Value for foo
After:  {'exists': 5, 'foo': 'Value for foo'}
'''

class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)

data = LoggingLazyDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)

'''
exists: 5
Called __getattr__(foo)
foo:    Value for foo
foo:    Value for foo
'''

# __getattribute__. This special method is called every time an attribute is
# accessed on an object, even in cases where it does exist in the
# attribute dictionary. This enables you to do things like check
# global transaction state on every property access.
# Here, I define ValidatingDB to log each time __getattribute__ is called:

class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

data = ValidatingDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)

'''
Called __getattribute__(exists)
exists: 5
Called __getattribute__(foo)
foo:    Value for foo
Called __getattribute__(foo)
foo:    Value for foo
'''

class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError('%s is missing' % name)
        pass  # ...

data = MissingPropertyDB()
data.bad_name

'''
AttributeError: bad_name is missing
'''

data = LoggingLazyDB()
print('Before:     ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))
print('After:      ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))

'''
Before:      {'exists': 5}
Called __getattr__(foo)
foo exists:  True
After:       {'exists': 5, 'foo': 'Value for foo'}
foo exists:  True
'''

# In the example above, __getattr__ is only called once.
# In contrast, classes that implement __getattribute__ will have that method
# called each time hasattr or getattr is run on an object.

data = ValidatingDB()
print('foo exists: ', hasattr(data, 'foo'))
print('foo exists: ', hasattr(data, 'foo'))

'''
Called __getattribute__(foo)
foo exists:  True
Called __getattribute__(foo)
foo exists:  True
'''

# Unlike retrieving an attribute with __getattr__ and __getattribute__,
# there’s no need for two separate methods. The __setattr__ method is always
# called every time an attribute is assigned on an instance
# (either directly or through the setattr built-in function).

class SavingDB(object):
    def __setattr__(self, name, value):
        # Save some data to the DB log
        # ...
        super().__setattr__(name, value)

class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)

data = LoggingSavingDB()
print('Before: ', data.__dict__)
data.foo = 5
print('After:  ', data.__dict__)
data.foo = 7
print('Finally:', data.__dict__)

'''
Before:  {}
Called __setattr__(foo, 5)
After:   {'foo': 5}
Called __setattr__(foo, 7)
Finally: {'foo': 7}
'''

class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        return self._data[name]

# This requires accessing self._data from the __getattribute__ method. However, if you actually try to do that, Python will recurse until it reaches its stack limit, and then it’ll die.

data = BrokenDictionaryDB({'foo': 3})
data.foo

'''
Called __getattribute__(foo)
Called __getattribute__(_data)
Called __getattribute__(_data)
...
Traceback ...
RuntimeError: maximum recursion depth exceeded
'''

# The solution is to use the super().__getattribute__ method on your instance
# to fetch values from the instance attribute dictionary. This avoids the recursion.

class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]

# Similarly, you’ll need __setattr__ methods that modify attributes on an
# object to use super().__setattr__.
