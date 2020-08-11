#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from urllib import request
from http.cookiejar import MozillaCookieJar

# 保存 cookie
cookiejar = MozillaCookieJar('cookie.txt')
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://www.baidu.com')
# 加上 ignore_discard 表示快过期的也保存
cookiejar.save(ignore_discard=True)

# 加载 cookie
cookiejar.load()