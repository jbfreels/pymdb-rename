import pathlib
import unittest
from os import path, unlink

from context import core as core
from core import Imdb, Movie
from core.Config import config


class TestMovie(unittest.TestCase):
    data_path = 'tests/data'
    data_out_path = 'tests/data/output'
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
        config.action = "copy"
        for i in self.files:
            fn = self.files[i]['file']
            dfn = path.join(self.data_path, path.basename(fn))

            m = self.__create_movie(dfn)

            ofn = path.join(self.data_out_path, path.basename(
                m.get_formatted_name(True)))
            m.do_output(self.data_out_path)
            self.assertTrue(path.exists(ofn))
            unlink(ofn)
            unlink(dfn)

    def test_move(self):
        config.action = "move"
        for i in self.files:
            fn = self.files[i]['file']
            dfn = path.join(self.data_path, path.basename(fn))

            m = self.__create_movie(dfn)

            ofn = path.join(self.data_out_path, path.basename(
                m.get_formatted_name(True)))
            m.do_output(self.data_out_path)
            self.assertFalse(path.exists(dfn))
            self.assertTrue(path.exists(ofn))
            unlink(ofn)

    def test_test(self):
        config.action = "test"
        for i in self.files:
            fn = self.files[i]['file']
            dfn = path.join(self.data_path, path.basename(fn))

            m = self.__create_movie(dfn)

            ofn = path.join(self.data_out_path, path.basename(
                m.get_formatted_name(True)))
            m.do_output(self.data_out_path)
            self.assertFalse(path.exists(ofn))
            self.assertTrue(path.exists(dfn))
            unlink(dfn)

    def __create_movie(self, fn):
        pathlib.Path(fn).touch(exist_ok=True)
        m = Movie.Movie(fn)
        m.title, m.year = Imdb.Imdb(m.name).fetch_movie()
        return m
