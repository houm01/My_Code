#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import sys


sum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        sum += int(line)

print(sum)