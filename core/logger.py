import logging
from core.config import config

from os import path

formatter = logging.Formatter (config['logger']['format'])
logger = logging.getLogger ()
logger.setLevel(logging.NOTSET)

logfile = logging.FileHandler (config['logger']['path'])
logfile.setLevel (eval (config['logger']['filelevel']))
logfile.setFormatter (formatter)
logger.addHandler (logfile)

logout = logging.StreamHandler ()
logout.setLevel (eval (config['logger']['stdoutlevel']))
logout.setFormatter (formatter)
logger.addHandler (logout)

logger.info ("starting")