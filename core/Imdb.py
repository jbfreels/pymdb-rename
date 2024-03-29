import logging

from imdb import IMDb
from similarity.damerau import Damerau


class Imdb:
    logger = logging.getLogger(__name__)

    def __init__(self, name):
        self.IMDb = IMDb()
        self.matches = []
        self.name = name

    def fetch_movie(self):
        self.__find_movies()
        return self.__best_match()

    def __find_movies(self):
        res = self.IMDb.search_movie(self.name)
        self.matches = []
        for r in res:
            if r["kind"] == "movie":
                n = r["title"]
                try:
                    y = r["year"]
                except Exception:
                    nm = self.IMDb.get_movie(r.movieID)
                    y = nm['year']
                self.matches.append(f"{n} {y}")

    def __best_match(self):
        if len(self.matches) == 0:
            return None

        dl = Damerau()
        ops = []
        for m in self.matches:
            if self.name.upper() == m.upper():
                return m.rsplit(" ", 1)
            else:
                ops.append(dl.distance(self.name.upper(), m.upper()))
        i = int(ops.index(min(ops)))

        if self.matches[i] != "":
            return self.matches[i].rsplit(" ", 1)
