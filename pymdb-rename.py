#!/usr/bin/env python3
import atexit
import sys
from os import path

from core import FileUtils, get_logger
from core.Config import config
from core.Imdb import Imdb
from core.Movie import Movie

logger = get_logger("pymdb-rename")
logger.info("starting")
logger.debug(config)


def usage():
    print("pymdb-rename.py <INPUT_FILE>")


def exit_handler():
    logger.info("quitting")


atexit.register(exit_handler)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        exit(1)

    infile = sys.argv[1]
    if not path.exists(infile):
        logger.error("input file does not exist")
        exit(1)

    try:
        movie = Movie(infile)
    except OSError as ex:
        logger.error(f"error determining media file from input\n{ex}")
        exit(1)

    if movie.ext not in config.movie_exts:
        logger.error("looks like input isn't a media file")
        exit(1)

    try:
        imdb = Imdb(movie.name)
        movie.title, movie.year = imdb.fetch_movie()
    except Exception as ex:
        logger.error(f"movie.name: '{movie.name}' could not be found.\n{ex}")
        sys.exit(1)

    if movie.title is not None:
        strout = "{} -> {}".format(movie.filename, movie.get_formatted_name(True))
        if config.action.upper() == "TEST":
            strout = "[TEST] " + strout
        print(strout)
        try:
            movie.do_output()
        except IOError as e:
            logger.error(str(e))

        if FileUtils.containsChars(movie.title, config.warnings["invalid_url_chars"]):
            logger.warning("output filename contains invalid URL characters!")
    else:
        print("couldn't find a match")
        exit(1)

    exit(0)
