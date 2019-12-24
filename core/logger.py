import logging
from core.Config import config
import atexit

from os import path

def exit_handler ():
  logger.debug ("quitting")

atexit.register (exit_handler)

formatter = logging.Formatter (config.logger['format']) #config['logger']['format'])
logger = logging.getLogger ()
logger.setLevel(logging.NOTSET)

logfile = logging.FileHandler (config.logger['path'])
logfile.setLevel (eval (config.logger['filelevel']))
logfile.setFormatter (formatter)
logger.addHandler (logfile)

logout = logging.StreamHandler ()
logout.setLevel (eval (config.logger['stdoutlevel']))
logout.setFormatter (formatter)
logger.addHandler (logout)

logger.debug ("starting")
logger.debug (config)