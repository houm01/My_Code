#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import sys, os


def lister(root):
    for (thisdir, subshere, fileshere) in os.walk(root):
        print('[' + thisdir + ']')
        print(subshere)
        for fname in fileshere:
            path = os.path.join(thisdir, fname)
            print(path)


if __name__ == '__main__':
    lister(sys.argv[1])
