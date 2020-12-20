#!/usr/bin/env python3

import re

regexes = [
    re.compile(p)
    for p in ['this', 'that']
]

text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')
    
    if regex.search(text):
        print('match!')
    else:
        print('no match')


# 输出
# [Running] /usr/bin/env python3 "/Users/houmingming/My_Code/Python-KB/Standard-Library/re/re_simple_compiled.py"
# Text: 'Does this text match the pattern?'

# Seeking "this" -> match!
# Seeking "that" -> no match

# [Done] exited with code=0 in 0.075 seconds

# 说明
# 没看懂！