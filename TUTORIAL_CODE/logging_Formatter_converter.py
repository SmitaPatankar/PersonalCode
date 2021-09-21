import time
import logging

logging.Formatter.converter = time.gmtime
logging.basicConfig(
    format='%(asctime)s',
    handlers=[logging.FileHandler("logging_Formatter_converter_demo.log")],
    level=1
)
for i in range(100):
    logging.error(i)

# using formatter - US time
# 2019-04-30 06:58:17,299

# without formatter - Indian time
# 2019-04-30 12:28:38,778
