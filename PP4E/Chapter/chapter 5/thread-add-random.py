#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import threading, time

count = 0

def adder():
    global count
    count = count + 1
    time.sleep(0.5)
    count = count + 1

threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(count)