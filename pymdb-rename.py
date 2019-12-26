import sys
from os import path

from core.Config import config
from core.logger import logger
from core.Movie import Movie


def usage():
    print("pymdb-rename.py <INPUT_FILE>")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        exit(1)

    infile = sys.argv[1]
    if not path.exists(infile):
        logger.error("input file '{}' does not exist".format(infile))
        exit(1)

    movie = Movie(infile)

    if not movie.ext in config.movie_exts:
        logger.error("looks like input isn't a media file")
        exit(1)

    if movie.name != None:
        print("Looks like: " +
              config.movie_format.format(n=movie.name, y=movie.year))
    else:
        print("couldn't find a match :(")
        exit(1)

    exit(0)
