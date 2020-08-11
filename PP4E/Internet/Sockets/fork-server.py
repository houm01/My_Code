#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import os, time, sys
from socket import *

myHost = ''
myPort = 50007


sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def now():
    return time.ctime(time.time())


activeChildren = []


def reapChildren():
    while activeChildren:
        pid, stat = os.waitpid(0, os.WNOHANG)
        if not pid:
            break
        activeChildren.remove(pid)


def handleClinet(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = 'Echo => %s at %s' %(data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)


def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connection by', address, end = ' ')
        print('at', now())
        reapChildren()
        childPid = os.fork()
        if childPid == 0:
            handleClinet(connection)
        else:
            activeChildren.append(childPid)


dispatcher()