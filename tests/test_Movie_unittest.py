import unittest
from os import path

from context import core as core
from core import Movie


class TestMovie(unittest.TestCase):
    files = {
        "0": {
            "title": "The Goonies 1985",
            "year": "1985",
            "file": "./movies/the.goonies.1985.avi"
        },
        "1": {
            "title": "The Matrix 1999",
            "year": "1999",
            "file": "/mnt/nas/new movies/the_matrix-1999.mp4"
        },
        "2": {
            "title": "Addams Family Values 1993",
            "year": "1993",
            "file": "addams-family-values(1993).mkv"
        }
    }

    def test_movie(self):
        for i in self.files:
            fn = self.files[i]['file']
            title = self.files[i]['title']
            year = self.files[i]['year']
            m = Movie.Movie(fn)
            self.assertEqual(m.path, fn)
            self.assertEqual(m.dirname, path.dirname(fn))
            self.assertEqual(m.filename, path.basename(fn))
            self.assertIn(m.name.upper(), title.upper())
            self.assertIn(m.ext, fn)
            self.assertEqual(m.year, year)
