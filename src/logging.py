
import logging
from .conf.general_conf import LOGGING_LEVEL_S, LOGGING_LEVEL_F, LOGGER_NAME

print(f'Start logger with levels:\n\tTerminal = {LOGGING_LEVEL_S}\n\tFile = {LOGGING_LEVEL_F}')

fmt = '[%(asctime)s] %(levelname)s - %(filename)s:%(lineno)s - %(message)s'
# datefmt = '%Y-%m-%d %I:%M:%S %p'
datefmt = '%Y-%m-%d %H:%M:%S'

# define logger
logger = logging.getLogger(LOGGER_NAME)
# allow all
logger.setLevel(logging.DEBUG)

# stream
s_handler = logging.StreamHandler()
s_handler.setLevel(LOGGING_LEVEL_S)
s_format = logging.Formatter(fmt)
s_handler.setFormatter(s_format)
logger.addHandler(s_handler)

# file
f_handler = logging.FileHandler('server.log')
f_handler.setLevel(LOGGING_LEVEL_F)
f_format = logging.Formatter(fmt, datefmt)
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)


if True:
    logger.debug('THIS IS A TEST DEBUG')
    logger.info('THIS IS A TEST INFO')
    logger.warning('THIS IS A TEST WARNING')
    logger.error('THIS IS A TEST ERROR')
    logger.critical('THIS IS A TEST CRITICAl')
