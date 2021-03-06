import unittest
from os import makedirs, path, unlink

from context import core as core
from core import FileUtils, Imdb, Movie
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
        },
        "3": {
            "title": "Avatar 2009",
            "year": "2009",
            "file": "avatar(2009).avi",
            "folder": "Avatar",
            "subs": True
        },
        "4": {
            "title": "Terminator Dark Fate 2019",
            "year": "2019",
            "file": "terminator_dark_fate_2019.mkv",
            "folder": "terminator dark fate [2019]",
            "subs": True
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
            subs = None
            asDir = False
            if 'subs' in self.files[i]:
                asDir = True
                folder = self.files[i]['folder']
                subs = path.join(self.data_path, folder, "Subs")
                makedirs(subs)
                dfn = path.join(self.data_path, folder, path.basename(fn))
            else:            
                dfn = path.join(self.data_path, path.basename(fn))

            m = self.__create_movie(dfn, asDir)

            ofn = path.join(self.data_out_path,
                            path.basename(m.get_formatted_name(True)))
            m.do_output(self.data_out_path)
            self.assertFalse(path.exists(dfn))
            self.assertTrue(path.exists(ofn))

            if subs:
                self.assertFalse(path.exists(subs))

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

    def __create_movie(self, fn, asDir=False):
        FileUtils._create_dummy_file(fn, 22)
        if asDir:
            m = Movie.Movie(path.dirname(fn))
        else:
            m = Movie.Movie(fn)
        m.title, m.year = Imdb.Imdb(m.name).fetch_movie()
        return m
