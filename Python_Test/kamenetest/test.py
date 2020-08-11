#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from kamene import *


def ping(ip):
    request = IP(dst=ip)/ICMP()
    jieguo = sr1(request, timeout=2, verbose=False)
    if jieguo:
        print(ip, 'tong',)
    else:
        print(ip, 'butong',)


with open('ip_list', 'r+') as f:
    for i in f.read().splitlines():
        print(i)

        # ping(ip)

ip_list = open('ip_list', 'r')
for ip in ip_list:
    print(ip)
    # ping(ip)

ip_list.close()



