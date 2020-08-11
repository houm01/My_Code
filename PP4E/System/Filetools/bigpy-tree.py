#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import sys, os, pprint


trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python31\lib'
else:
    dirname = '/usr/local/lib/python3.7/site-packages'  # /usr/local/lib/python3.7/site-packages

allsizes = []
for (thisDir, subsHere, fileHere) in os.walk(dirname):
    if trace:
        print(thisDir)
    for filename in fileHere:
        if trace:
            print('...', filename)
        fullname = os.path.join(thisDir, filename)
        fullsize = os.path.getsize(fullname)
        allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])