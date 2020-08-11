#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import os, time, sys


mypid = os.getpid()
parentpid = os.getpid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' %(mypid, parentpid, sys.argv[1]))

for i in range(2):
    time.sleep(3)
    recv = input()
    time.sleep(3)
    send = 'Child %d got: [%s]' % (mypid, recv)
    print(send)
    sys.stdout.flush()
