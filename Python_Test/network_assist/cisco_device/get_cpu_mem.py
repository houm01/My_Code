#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import re
import os

os.chdir("/Users/houmingming/Downloads/test")

for x in os.listdir():
    # print(x)
    with open(x) as f:
        raw_text = f.read()
        cpu_usage = re.search('five minutes: (.*)', raw_text).groups()[0]

        try:
            memory_total = (
            ([x for x in (''.join(re.search('Processor Pool Total:(.*)', raw_text).groups())).split(' ') if x != ''])[
                0])
            memory_usage = (([x for x in (''.join(re.search('Processor Pool Total:(.*)', raw_text).groups())).split(' ') if x != ''])[2])
            memory_per = '%.2f%%' % (int(memory_usage)/int(memory_total))
        except AttributeError:
            pass
    print(x, cpu_usage, memory_per)


        # print(f.read())



# print(os.listdir())
