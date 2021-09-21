import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    format='levelname=%(levelname)s message=%(message)s',
    handlers=[RotatingFileHandler("RotatingHandler_demo.log", maxBytes=100, backupCount=3)],
    level=1
)
for i in range(100):
    logging.error(i)

# upto one main and <<backupCount>> backup files created where, rest all older data vanishes
# new file created when old file exceeds <<maxBytes>> bytes
