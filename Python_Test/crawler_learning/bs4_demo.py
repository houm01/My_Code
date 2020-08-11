#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://shimo.im/desktop')
bs = BeautifulSoup(html.read(), 'html.parser')   # html.parser 是 Python3 中的一个解析器，不需要单独安装，还有 lxml 解析器
print(bs.meta)

