# -*- coding: utf-8 -*-
import os
import shutil
import sys

from core.Config import Config
from core.ProgressBar import ProgressBar

pbar = ProgressBar("")


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
