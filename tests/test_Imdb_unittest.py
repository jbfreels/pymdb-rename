import unittest

from context import core as core
from core import Imdb


class TestImdb(unittest.TestCase):
    movies = [
        "The Goonies 1985"
    ]

    def test_fetch(self):
        for movie in self.movies:
            i = Imdb.Imdb(movie)
            t, y = movie.rsplit(" ", 1)
            rt, ry = i.fetch_movie()
            self.assertEqual(rt, t)
            self.assertEqual(ry, y)


if __name__ == "__main__":
    unittest.main()
