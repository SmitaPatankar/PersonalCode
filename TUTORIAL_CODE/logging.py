import logging # builtin
# logging levels
# debug - diagnosing
# info - confirmation
# warning - something unexpected but s/w is working fine (default)
# error - s/w not able to perform a function
# critical - program can't continue to run

# logging.debug('abc')  # not shown
#
# logging.warning('def')  # shown  # WARNING:root:def  # root means no logger is set

# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug('pqr')  # shown  # DEBUG:root:pqr

# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logging.debug('blah')  # goes to file # DEBUG:root:blah
# logging.info('blah')  # goes to file # INFO:root:blah

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('blahblah')  # in file # 2019-11-18 14:51:29,723:INFO:blahblah

# log record attributes
# official doc

# when module is imported, code from that module runs