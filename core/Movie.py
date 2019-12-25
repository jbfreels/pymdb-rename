import re
from os import path

import core.Imdb as imdb
from core.logger import logger


class Movie:

    movie = None

    def __init__(self, infile):

        self.path = infile
        self.dirname = path.dirname(infile)
        self.filename = path.basename(infile)
        self.name, self.ext = path.splitext(self.filename)
        self._fix_name()
        self._get_year_from_name()

        logger.debug(self.__dict__)

        i = imdb.Imdb(self.name)
        logger.info(i.movie)
        logger.info(i.year)

    def _get_year_from_name(self):

        m = re.match(r".*([1-3][0-9]{3})", self.name)
        if m is not None:
            self.name = m.group(0)
            self.year = m.group(1)
        else:
            self.year = "0000"

    def _fix_name(self):
        rep_chars = ['<', '>', '*', '?', '|',
                     '\\', '/', '"', ':', '.']

        for c in rep_chars:
            self.name = self.name.replace(c, " ")
