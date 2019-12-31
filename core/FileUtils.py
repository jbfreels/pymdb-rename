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
            size = os.path.getsize(os.path.join(folder, f)) / 1024**2
            logger.debug("{} is {} MB".format(f, size))
            if size > min_size:
                # this is a hack to see if file is the main media file
                # or not.  TODO replace this with a string compare
                files.extend([f])
                logger.debug("file meets size requirement")
            else:
                logger.debug(
                    "file does not meet size requirement {}".format(size))

    if len(files) == 1:
        return os.path.join(folder, files[0])

    return file


def cleanFolder(folder):
    if config.clean['enabled'] == True:
        for f in os.listdir(folder):
            path = os.path.join(folder, f)
            if os.path.isdir(path):
                continue

            n, ext = os.path.splitext(f)

            if not ext:
                continue

            if ext in config.clean['exts']:
                if config.action != "test":
                    os.remove(path)
                logger.debug('{} removed'.format(f))
                continue

            size = os.path.getsize(os.path.join(folder, f)) / 1024**2
            if size > config.clean['max_size']:
                logger.debug('{} ignoring, exceeds max_size')
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
