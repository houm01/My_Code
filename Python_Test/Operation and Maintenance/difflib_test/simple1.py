#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import difflib


text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
"""

text1_lines = text1.splitlines()

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5
"""

text2_lines = text2.splitlines()

# 直接比较
# d = difflib.Differ()
# diff = d.compare(text1_lines, text2_lines)
# print('\n'.join(list(diff)))

# 生成 HTML 页面
d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))