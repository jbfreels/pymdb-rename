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
        self.in_is_dir = False

        if path.isdir(inpath):
            self.in_is_dir = True
            FileUtils.cleanFolder(inpath)
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
            output = path.join(outpath, path.basename(
                self.get_formatted_name(True)))
        else:
            output = self.get_formatted_name(True)

        if config.action.upper() == "COPY":
            self.__copy(output)
        elif config.action.upper() == "MOVE":
            self.__move(output)
        elif config.action.upper() == "TEST":
            self.__test(output)
        else:
            self.logger.error("unknown action '{}'".format(config.action))
        return None

    def __copy(self, output):
        try:
            self.logger.info("starting data copy")
            self.logger.info("{} -> {}".format(self.path, output))
            FileUtils.copyFile(self.path, output)
        except FileExistsError as e:
            self.logger.error(e)
        except FileNotFoundError as e:
            self.logger.error(e)
        else:
            return output
        return None

    def __move(self, output):
        try:
            os.rename(self.path, output)
            self.logger.info("removing input file")
            if self.in_is_dir:
                if FileUtils.isFolderEmpty(self.dirname):
                    os.rmdir(self.dirname)
                    self.logger.info("removed empty input folder")
        except OSError as e:
            self.logger.error("input file could not be removed")

    def __test(self, output):
        self.logger.info("{} -> {}".format(self.path, output))

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
