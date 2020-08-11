#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import nmap

nm = nmap.PortScanner()
nm.scan('192.168.100.0/24', arguments='-sn')
# print(nm.all_hosts())
for i in nm.all_hosts():
    print(i)