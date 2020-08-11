#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import _thread as thread


stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId] = True

for i in range(10):
    thread.start_new_thread(counter, (i, 100))

while False is exitmutexes:
    pass

print('Main thread exiting.')