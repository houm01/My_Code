#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


# import os
#
#
# for line in os.popen('ls /'):
#     # print(line[:-1])
#     pass
#
# print(os.popen('ls /').readlines())

# import glob
#
#
# print(glob.glob('/Users/houmingming/*'))

import os


for (dirname, subshere, fileshere) in os.walk('/'):
    print( '[' + dirname + ']')
    for fname in fileshere:
        print(os.path.join(dirname, fname))