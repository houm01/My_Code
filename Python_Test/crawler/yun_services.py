#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import requests


url = 'https://item.jd.com/100006914135.html'

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")

