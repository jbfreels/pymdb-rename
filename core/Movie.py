import re
from os import path

import core.Imdb as imdb
from core.Config import config
from core.logger import logger


class Movie:
    def __init__(self, infile):
        self.title = None
        self.year = None
        self.path = infile
        self.dirname = path.dirname(infile)
        self.filename = path.basename(infile)
        self.name, self.ext = path.splitext(self.filename)
        self.name = self.__fix_name(self.name)
        self.__parse_fixed_name()

        logger.debug(self.__dict__)

    def get_formatted_name(self):
        return config.movie_format.format(n=self.title, y=self.year)

    def get_output_filename(self):
        return self.get_formatted_name() + self.ext

    def __parse_fixed_name(self):
        m = re.match(r".*([1-3][0-9]{3})", self.name)
        if m is not None:
            self.name = m.group(0)
            self.year = m.group(1)
        else:
            self.year = None

    def __fix_name(self, name):
        rep_chars = ['<', '>', '*', '?', '|',
                     '\\', '/', '"', ':', '.',
                     '[', ']', '_', '-', '(', ')',
                     "1080p", "1080", "720p", "720", 
                     "  "]

        for c in rep_chars:
            name = name.replace(c, " ")

        return name
