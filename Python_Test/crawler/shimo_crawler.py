#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from urllib.request import urlopen

html = urlopen("https://shimo.im/desktop")

print(html.read())




