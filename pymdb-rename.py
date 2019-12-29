import atexit
import sys
from os import path

from core import FileUtils, get_logger
from core.Config import config
from core.Imdb import Imdb
from core.Movie import Movie

logger = get_logger('pymdb-rename')
logger.info("starting")
logger.debug(config)

def usage():
    print("pymdb-rename.py <INPUT_FILE>")


def exit_handler():
    logger.info('quitting')


atexit.register(exit_handler)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        exit(1)

    infile = sys.argv[1]
    if not path.exists(infile):
        logger.error("input file does not exist")
        exit(1)

    movie = Movie(infile)

    if not movie.ext in config.movie_exts:
        logger.error("looks like input isn't a media file")
        exit(1)

    imdb = Imdb(movie.name)
    movie.title, movie.year = imdb.fetch_movie()

    if movie.title != None:
        print("{} -> {}".format(movie.filename, movie.get_output_filename()))
        movie.do_output()
    else:
        print("couldn't find a match :(")
        exit(1)

    exit(0)
