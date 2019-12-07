import logging
from core.config import config

from os import path

logger = logging.getLogger ('pymdb-rename')
logger.setLevel (eval (config['logger']['stdoutlevel']))
formatter = logging.Formatter (config['logger']['format'])

logfile = logging.FileHandler (config['logger']['path'])
logfile.setLevel (eval (config['logger']['filelevel']))
logfile.setFormatter (formatter)

logout = logging.StreamHandler ()
logout.setLevel (eval (config['logger']['stdoutlevel']))
logout.setFormatter (formatter)

logger.addHandler (logfile)
logger.addHandler (logout)

logger.info ("starting")