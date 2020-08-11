#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# 笔记：https://www.notion.so/houm01/fb11e5a506c846ad9053083d27a65a60（分享了我的Notion权限的才能打开）
# 代码放一起了，使用时要分别注释
# 以下内容参考了《Python3标准库》一书

import re

# re.findall 会进行多重匹配
# 在分析 srx 策略的脚本中，有用到 findall，非常好用
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))


# re.finditer 示例
# 注意 .start .end 的用法
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(text[s:e], s, e))

