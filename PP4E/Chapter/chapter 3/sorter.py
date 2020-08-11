#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import sys


lines = sys.stdin.readlines()
lines.sort()
for line in lines:
    print(line, end='')

