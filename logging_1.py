
import logging

logger = logging.getLogger(__name__)

try:
    print(1 / 0)
except:
    logger.exception("Log Zero Division")

# ZeroDivisionError: division by zero
# ___________________________________________________________

import time
from logging.handlers import TimedRotatingFileHandler

def create_timed_rotating_log(path):
    """"Какая_то непонятка"""
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(path,
                                       when='s',
                                       interval=5,
                                       backupCount=5)
    logger.addHandler(handler)

    for i in range(6):
        logger.info("This is a test!")
        time.sleep(5)

if __name__ == "__main__":
    log_file = "timed_rotation.log"
    create_timed_rotating_log(log_file)