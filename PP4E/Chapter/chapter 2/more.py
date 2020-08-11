#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

# 分割文本字符串或文本文件


def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('more?') not in ['y', 'Y']:
            break


if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(), 10)
