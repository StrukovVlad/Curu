
import logging
# ______________________________________________________________________
"""Create logger"""
"""Создаем экземпляр логгера с именем 'example App'.Или
 возращаем объект логгера с именем 'example App'"""

logger = logging.getLogger('example App')

"""Устанавливаем у логера уровень логирования.Например INFO"""

logger.setLevel(logging.INFO)
# _________________________________________________________________________
"""Create handlers (ch ,fh) and set level to debug"""
"""Создаем объект обработчика лог файла и устанавливаем уровень 
логирования как пример"""

ch = logging.StreamHandler()
fh = logging.FileHandler('new-snake.log')
ch.setLevel(logging.WARNING)
fh.setLevel(logging.ERROR)
# ______________________________________________________________________________
"""Create formatters and add it to handlers"""
"""Форматируем объект обработчика"""

c_formatter = logging.Formatter('%(name)s -%(levelname)s -%(message)s')
f_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
ch.setFormatter(c_formatter)
fh.setFormatter(f_formatter)
# _________________________________________________________________________________
"""Add handlers to the logger"""

logger.addHandler(ch)
logger.addHandler(fh)
# __________________________________________________________________________________
"""application code"""

logger.debug('debug message')
logger.info('info message')
logger.error('error message')
logger.warning('warning message')
# ____________________________________________________________________________________
"""Создаем лог"""

logging.basicConfig(filename = 'sample.log',filemode = 'w',level = logging.INFO)

# basicConfig-это функция метода logging
# level=logging.INFO- установка уровня логирования
# filemode = 'w' - ставим возможность перезаписывать лог


import logging
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