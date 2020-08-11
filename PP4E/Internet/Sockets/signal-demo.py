#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import sys, signal, time


def now():
    return time.asctime()


def onSignal(signum, stackframe):
    print('Got signal', signum, 'at', now())
    if signum == signal.SIGCHLD:
        print('sigchld caught')
        signal.signal(signal.SIGCHLD, onSignal)


signum = int(sys.argv[1])
signal.signal(signum, onSignal)
while True:
    signal.pause()

