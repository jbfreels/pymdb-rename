from os import path
from core.logger import logger

class Movie:

    def __init__(self, infile):

        self.path = infile
        self.dirname = path.dirname (infile)
        self.filename = path.basename (infile)
        self.name, self.ext = path.splitext (self.filename)
        self.movie = None
        self.year = None

        logger.debug (self.__dict__)
