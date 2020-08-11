#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from selenium import webdriver


drive = webdriver.Chrome()  # 调用Chrome浏览器
drive.get('https://www.zhihu.com')
print(drive.page_source)  # 查看网页源代码

