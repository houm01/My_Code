#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


def later():
    import sys
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')


if __name__ == '__main__':
    later()