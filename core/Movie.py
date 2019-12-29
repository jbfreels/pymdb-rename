import os
import re
from os import path

import core.Imdb as imdb
from core import FileUtils
from core.Config import config

from core import get_logger


class Movie:
    logger = get_logger(__name__)

    def __init__(self, infile):
        self.title = None
        self.year = None
        self.path = infile
        self.dirname = path.dirname(infile)
        self.filename = path.basename(infile)
        self.name, self.ext = path.splitext(self.filename)
        self.name = self.__fix_name(self.name)
        self.__parse_fixed_name()

        self.logger.debug(self.__dict__)

    def get_formatted_name(self):
        return config.movie_format.format(n=self.title, y=self.year)

    def get_output_filename(self):
        return path.join(config.out_path, self.get_formatted_name() + self.ext)

    def do_output(self):
        try:
            self.logger.info("copying data")
            FileUtils.copyFile(self.path, self.get_output_filename())
        except FileExistsError as e:
            self.logger.error(e)
        except FileNotFoundError as e:
            self.logger.error(e)
        else:
            if config.action.upper() == "MOVE":
                self.logger.info("removing input file")
                os.remove(self.path)

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
