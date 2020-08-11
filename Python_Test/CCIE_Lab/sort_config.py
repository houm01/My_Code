#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import os
import re

_nsre = re.compile('([0-9]+)')


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]

# 注意将文件目录换成自己放配置的目录
dir_config = '/Users/houmingming/cache/config/'

list1 = os.listdir(os.chdir(dir_config))

list1.sort(key=natural_sort_key)

print(list1)

Q2 = open('Q2+.txt', 'w')

for i in list1:
    if i != '.DS_Store':
        with open(dir_config + i) as ff:
            Q2.write(ff.read())
            print(ff.read())
    else:
        pass

Q2.close()

print('已完成')