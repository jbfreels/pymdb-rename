# -*- coding: utf-8 -*-
import glob
import os
import shutil
import sys
import fnmatch

from core.Config import config
from core.ProgressBar import ProgressBar
from core import get_logger

pbar = ProgressBar("")
logger = get_logger(__name__)


def findMovieInDir(folder):
    file = None
    files = []
    min_size = 300  # in MB

    for f in os.listdir(folder):
        name, ext = os.path.splitext(f)
        if ext in config.movie_exts:
            files.extend([f])

    if len(files) == 1:
        return os.path.join(folder, files[0])

    return file


def isFolderEmpty(folder):
    if not os.listdir(folder):
        return True
    else:
        return False


def cleanFolder(folder):
    if config.clean['enabled'] == True:
        for f in os.listdir(folder):
            path = os.path.join(folder, f)
            if os.path.isdir(path):
                continue

            n, ext = os.path.splitext(f)

            if ext in config.clean['exts']:
                if config.action != "test":
                    os.remove(path)
                logger.debug('{} removed'.format(f))
                continue

            size = os.path.getsize(os.path.join(folder, f)) / 1024**2
            if size > config.clean['max_size']:
                logger.debug('{} ignoring, exceeds max_size'.format(f))
                continue

            if size < config.clean['min_size']:
                if config.action != "test":
                    os.remove(path)
                logger.debug('{} removed, under min_size')
                continue


def copyFile(src, dst, follow_sym=True):
    if os.path.exists(dst):
        raise FileExistsError(
            "destination file exists: '{}'".format(dst))

    if not os.path.exists(os.path.dirname(dst)):
        raise FileNotFoundError(
            "destination folder doesn't exist: '{}'".format(os.path.dirname(dst)))

    if not follow_sym and os.path.islink(src):
        os.symlink(os.readlink(src), dst)
    else:
        size = os.stat(src).st_size
        with open(src, 'rb') as fsrc:
            with open(dst, 'wb') as fdst:
                _copy_file_obj(fsrc, fdst, callback=_copy_progress, total=size)
    return dst


def _copy_file_obj(fsrc, fdst, callback, total, length=16*1024):
    copied = 0
    while True:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)
        copied += len(buf)
        callback(copied, total)


def _copy_progress(p, t):
    pbar.calcUpdate(p, t)


def _create_dummy_file(fn, size):
    f = open(fn, "wb")
    f.seek((size*1024*1024)-1)
    f.write(b"\0")
    f.close()
