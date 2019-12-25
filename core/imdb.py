from imdb import IMDb
from similarity.damerau import Damerau

from core.Config import config
from core.logger import logger


class Imdb:

    year = None
    movie = None

    def __init__(self, name):

        self.IMDb = IMDb()
        self.matches = []
        self.name = name
        self.find_movies()

    def find_movies(self):

        res = self.IMDb.search_movie(self.name)
        self.matches = []
        for r in res:
            if (r['kind'] == 'movie'):
                n = r['title']
                try:
                    y = r['year']
                except:
                    y = "0000"
            self.matches.append("{} {}".format(n, y))
        self.best_match()

    def best_match(self):

        dl = Damerau()
        ops = []
        for m in self.matches:
            if (self.name.upper() == m.upper()):
                self.movie, self.year = m.rsplit(' ', 1)
            else:
                ops.append(dl.distance(self.name.upper(), m.upper()))
        i = int(ops.index(min(ops)))

        if self.matches[i] != "":
            self.movie, self.year = self.name.rsplit(' ', 1)
        else:
            self.movie, self.year = self.matches[i].rsplit(' ', 1)

    def get_formatted_name(self):

        return config.movie_format.format(n=self.name, y=self.year)
