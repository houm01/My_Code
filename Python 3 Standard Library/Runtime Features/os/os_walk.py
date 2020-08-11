#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import os
import sys


if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print(dir_name)
    sub_dirs = [n + '/' for n in sub_dirs]  # 加 / 标记
    contents = sub_dirs + files
    contents.sort()
    for c in contents:
        print('  {}'.format(c))