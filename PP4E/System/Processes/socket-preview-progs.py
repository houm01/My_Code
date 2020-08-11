#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from socket_preview import server, client  # import 使用有问题
import os, sys
from threading import Thread


mode = int(sys.argv[1])
if mode == 1:
    server()
elif mode == 2:
    client('client:process=%s' % os.getpid())
else:
    for i in range(5):
        Thread(target=client, args=('client:thread=%s' % i)).start()