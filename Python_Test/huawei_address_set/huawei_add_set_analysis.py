#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import os
import re

fin_dict = {}

os.chdir('/Users/houmingming/cache/huawei_address_set')
with open('address_set_demo.txt') as f:
    raw_text = f.read()

test = re.finditer('ip address-set (.*) type object([\s\S]*?)#', raw_text)
for match in test:
    cache = match.groups()[1].split('\n')
    cache.remove(cache[0])
    cache.remove(cache[-1])
    # print(cache)
    # for x in cache:
    #     print(x)


        # x.split(' ').remove('\n')
        # print(x.split(''))


        # print(x.split(' ').remove('\n'))
        # x.split(' ').remove(x.split(' ')[3])
        # print(x)


        # print(x.split(' ').remove(x.split(' ')[1]))
    # print(cache)

    fin_dict[match.groups()[0]] = match.groups()[1].split('\n')

print(fin_dict)


for key, value in fin_dict.items():
    pass
    # print(key, value)




