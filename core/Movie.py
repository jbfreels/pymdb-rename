import os
import re
from os import path

import core.Imdb as imdb
from core import FileUtils
from core.Config import config

from core import get_logger


class Movie:
    logger = get_logger(__name__)

    def __init__(self, inpath):
        self.title = None
        self.year = None

        if path.isdir(inpath):
            inpath = FileUtils.findMovieInDir(inpath)

            if not inpath:
                raise FileNotFoundError(
                    "could not determine input from folder")

        self.path = inpath
        self.dirname = path.dirname(inpath)
        self.filename = path.basename(inpath)
        self.name, self.ext = path.splitext(self.filename)
        self.name = self.__fix_name(self.name)
        self.__parse_fixed_name()

        self.logger.debug(self.__dict__)

    def get_formatted_name(self, withext=False):
        f = config.movie_format.format(n=self.title, y=self.year)
        if withext:
            return f + self.ext
        return f

    def do_output(self, outpath=None):
        if outpath:
            # called specifying an output folder (unit test)
            output = path.join(outpath, path.basename(self.get_formatted_name(True)))
        else:
            output = self.get_formatted_name(True)
        try:
            self.logger.info("copying data")
            FileUtils.copyFile(self.path, output)
        except FileExistsError as e:
            self.logger.error(e)
        except FileNotFoundError as e:
            self.logger.error(e)
        else:
            if config.action.upper() == "MOVE":
                self.logger.info("removing input file")
                os.remove(self.path)
            return output
        return None

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
