#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


import _thread as thread
exitstat = 0


def child():
    global exitstat
    exitstat += 1
    threadid = thread.get_ident()
    print('Hello from child', threadid, exitstat)
    thread.exit()
    print('never reached')


def parent():
    while True:
        thread.start_new_thread(child, ())
        if input() == 'q':
            break


if __name__ == '__main__':
    parent()