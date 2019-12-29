import unittest
from os import path, unlink
import pathlib

from context import core as core
from core import Movie
from core import Imdb


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

    def test_copy(self):
        for i in self.files:
            dpath = 'tests/data'
            dopath = 'tests/data/output'
            fn = self.files[i]['file']
            dfn = path.join(dpath, path.basename(fn))
            pathlib.Path(dfn).touch(exist_ok=True)
            m = Movie.Movie(dfn)
            m.title, m.year = Imdb.Imdb(m.name).fetch_movie()
            ofn = path.join(dopath, m.get_formatted_name(True))
            outFile = m.do_output(dopath)
            self.assertTrue(path.exists(ofn))
            unlink(ofn)            
