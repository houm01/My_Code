#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


import sys


sum = 0
for line in sys.stdin:
    sum += int(line)
print(sum)


