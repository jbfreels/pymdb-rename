import logging

from core.Config import config


def get_logger(mod):
    logger = logging.getLogger(mod)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(config.logger['path'])
    handler.setLevel(eval(config.logger['file']['level']))
    formatter = logging.Formatter(config.logger['file']['format'])
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.StreamHandler()
    handler.setLevel(eval(config.logger['stdout']['level']))
    formatter = logging.Formatter(config.logger['stdout']['format'])
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
