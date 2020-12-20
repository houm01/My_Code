#!/usr/bin/env python3

import re

text = 'absbsbsabdbsdbds'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))
    

# 输出  
# [Running] /usr/bin/env python3 "/Users/houmingming/My_Code/Python-KB/Standard-Library/re/re_findall.py"
# Found 'ab'
# Found 'ab'

# [Done] exited with code=0 in 0.055 seconds

# 说明
# re.findall 会返回所有匹配的字符串