#!/usr/bin/env python3
# 《Python3 标准库》的代码

import re


pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()


print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]
))


# 输出
# -------------------------
# [Running] /usr/bin/env python3 "/Users/houmingming/My_Code/Python-KB/Standard-Library/re/re_simple_match.py"
# Found "this"
# in "Does this text match the pattern?"
# from 5 to 9 ("this")

# [Done] exited with code=0 in 0.058 seconds


# 说明
# 在其他代码里试 match.re.pattern 和 match.string 发现没有这个属性，不知道这里的是啥意思？
# 知道了！
# match.pattern表示把 pattern部分，也就是匹配的表达式取出来了，string 同理