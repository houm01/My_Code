#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import sys, os, glob

dirname = '/usr/local/lib/python3.7/site-packages' if len(sys.argv) == 1 else sys.argv[1]


allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])