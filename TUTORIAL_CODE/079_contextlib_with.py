from threading import Lock
lock = Lock()
with lock:
    print('Lock is held')

# same as
lock.acquire()
try:
    print('Lock is held')
finally:
    lock.release()

import logging
def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')

my_function()
# Error log here

from contextlib import contextmanager
@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield  # with block's content will execute # exceptions will be reraised
    finally:
        logger.setLevel(old_level)


with debug_logging(logging.DEBUG):
    print('Inside:')
    my_function()
print('After:')
my_function()

'''
Inside:
Some debug data
Error log here
More debug data
After:
Error log here
'''

# with target
with open('/tmp/my_output.txt', 'w') as handle:
    handle.write('This is some data!')

# own target
@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')

logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')

# Error will print

