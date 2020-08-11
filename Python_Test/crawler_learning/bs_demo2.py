#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

namelist = bs.find_all('span', {'class': 'green'})

for name in namelist:
    print(name)
