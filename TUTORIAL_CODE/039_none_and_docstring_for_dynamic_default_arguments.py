from datetime import datetime
from time import sleep
import json


def log(message, when=datetime.now()):
    print('%s: %s' % (when, message))


log('Hi there!')
sleep(0.1)
log('Hi again!')

'''
2014-11-15 21:10:10.371432: Hi there!
2014-11-15 21:10:10.371432: Hi again!
'''

# date calculate once only when func is defined i.e.during module load
# The convention for achieving the desired result in Python
# is to provide a default value of None and to
# document the actual behavior in the docstring


def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))


log('Hi there!')
sleep(0.1)
log('Hi again!')

'''
2014-11-15 21:10:10.472303: Hi there!
2014-11-15 21:10:10.573395: Hi again!
'''


# Using None for default argument values is especially important when the
# arguments are mutable.


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# The dictionary specified for default will be shared by all calls to decode
# because default argument values are only evaluated once
# (at module load time).

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

'''
Foo: {'stuff': 5, 'meep': 1}
Bar: {'stuff': 5, 'meep': 1}
'''

assert foo is bar


def decode(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

'''
Foo: {'stuff': 5}
Bar: {'meep': 1}
'''
