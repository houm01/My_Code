#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import sys, signal, time


def now():
    return time.ctime(time.time())


def onSignal(signum, stackframe):
    print('Got signal', signum, 'at', now())


signum = int(sys.argv[1])
signal.signal(signum, onSignal)
while True:
    signal.pause()