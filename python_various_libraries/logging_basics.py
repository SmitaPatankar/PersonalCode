import logging
import time
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("test_logger")
logger.propagate = False
logger.setLevel("INFO")
if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s levelname=%(levelname)s message=%(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
    formatter.converter = time.gmtime
    file_handler = RotatingFileHandler(filename="test.log", maxBytes=1000000, backupCount=5)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")

# 2020-06-04 14:45:18 levelname=INFO version=1.1 message=info
# 2020-06-04 14:45:18 levelname=WARNING version=1.1 message=warning
# 2020-06-04 14:45:18 levelname=ERROR version=1.1 message=error
# 2020-06-04 14:45:18 levelname=CRITICAL version=1.1 message=critical
