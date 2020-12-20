#!/usr/bin/env python3

import re

text = 'abababsbsbsdsd'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}: {:d}'.format(
        text[s:e], s, e
    ))

# 输出
# [Running] /usr/bin/env python3 "/Users/houmingming/My_Code/Python-KB/Standard-Library/re/re_finditer.py"
# Found 'ab' at 0: 2
# Found 'ab' at 2: 4
# Found 'ab' at 4: 6

# [Done] exited with code=0 in 0.069 seconds

# 说明
# 