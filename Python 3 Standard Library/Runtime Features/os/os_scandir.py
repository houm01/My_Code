#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import os
import sys


for entry in os.scandir(sys.argv[1]):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print('{name} is {type}'.format(name=entry.name, type=typ))

