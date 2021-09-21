import logging
# logging.info('1')
# logging.basicConfig(filename='1.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')  # configuring root logger

print(__name__)
logger = logging.getLogger(__name__)  # module name  # if something is not set, will take from root
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('handler.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stream_handler = logging.StreamHandler()  # for console
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# file_handler.setLevel(logging.DEBUG)

logger.info('new')  # 2019-11-18 15:07:40,953:INFO:new

try:
    print(1/0)
except ZeroDivisionError:
    logger.exception('zerorrrrrrrrr')  # gives traceback
'''
in file

2019-11-18 15:25:27,047:__main__:ERROR:zerorrrrrrrrr
Traceback (most recent call last):
  File "D:/self study/python training/youtubepython/logging_1.py", line 18, in <module>
    print(1/0)
ZeroDivisionError: division by zero
'''


# logger has level
# logger has file and stream stream_handler
# handlers have formatters

'''
console
2019-11-18 15:28:47,198:__main__:ERROR:zerorrrrrrrrr
Traceback (most recent call last):
  File "D:/self study/python training/youtubepython/logging_1.py", line 21, in <module>
    print(1/0)
ZeroDivisionError: division by zero
'''
