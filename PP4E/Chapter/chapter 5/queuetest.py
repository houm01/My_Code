#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

numconsumers = 2
numproducers = 4
nummessages = 4

import _thread as thread, queue, time
safeprint = thread.allocate_lock()
dataqQueue = queue.Queue()


def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataqQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))


def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = dataqQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print('consumer', idnum, 'got=>', data)


if __name__ == '__main__':
    for i in range(nummessages):
        thread.start_new_thread(consumer, (i,))
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((numproducers-1) * nummessages) + 1)
    print('Main thread exit.')