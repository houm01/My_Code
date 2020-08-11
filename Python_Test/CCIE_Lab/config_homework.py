#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


import re
import time
import telnetlib
from socket import *


def port_scaner(host):
    # 以下代码参考自：https://zhuanlan.zhihu.com/p/31042201
    # host = sys.argv[1]
    host = host
    # protstrs = sys.argv[2].splist('-')
    # portstrs = '34000-35000'

    # start_port = int(portstrs[0])
    start_port = 34000
    end_port = 35000
    # end_port = int(portstrs[1])

    target_ip = gethostbyname(host)
    opened_ports = []

    for port in range(start_port, end_port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            opened_ports.append(port)
    print('扫描到开放的端口如下\n')
    print(opened_ports)
    return opened_ports


def telnet_get_config(host, port):
    tn = telnetlib.Telnet(host, port, timeout=3)
    time.sleep(1)
    tn.write(b'\n')
    time.sleep(1)
    tn.read_until(b"R")
    tn.write('enable'.encode('ascii') + b'\n')
    time.sleep(1)
    tn.write('terminal length 0'.encode('ascii') + b'\n')
    time.sleep(1)
    tn.write('show running-config'.encode('ascii') + b'\n')
    time.sleep(3)  # 最好用5秒能将 show running 输出完
    tn.write('terminal no length'.encode('ascii') + b'\n')
    time.sleep(1)
    show_running = tn.read_very_eager().decode()
    tn.close()
    return show_running


def telnet_get_sw_config(host, port):
    tn = telnetlib.Telnet(host, port, timeout=3)
    time.sleep(1)
    tn.write(b'\n')
    time.sleep(1)
    tn.read_until(b"sw")
    tn.write('enable'.encode('ascii') + b'\n')
    time.sleep(1)
    tn.write('terminal length 0'.encode('ascii') + b'\n')
    time.sleep(1)
    tn.write('show running-config'.encode('ascii') + b'\n')
    time.sleep(3)  # 最好用5秒能将 show running 输出完
    tn.write('terminal no length'.encode('ascii') + b'\n')
    time.sleep(1)
    show_running = tn.read_very_eager().decode()
    tn.close()
    return show_running


if __name__ == '__main__':
    print('\n程序开始运行，请确保已经用CRT或Putty打开了所有设备,否则部分设备将获取不成功\n')
    print('每台设备需要30秒左右\n')
    print('如果程序长时间未自动结束，请手动按 ctrl+c 退出程序')
    print('-----------------------------------------------------------------')
    host = input('请输入您的模拟器IP:\n')
    not_get_port = []
    # port_test = ['34075, 34076']
    for i in port_scaner(host):
    # for i in port_test:
        try:
            hostname = re.search('hostname ([A-Za-z0-9]*)', telnet_get_config(host, i)).groups()[0]
            filename = hostname + '.txt'
            file = open(filename, 'w')
            print('\n正在获取的设备是:' + hostname)
            file.write(telnet_get_config(host, i))
            file.close()
        except BaseException as e:
            print('未成功获取的设备端口:' + str(i))
            hostname_sw = re.search('hostname ([A-Za-z0-9]*)', telnet_get_config(host, i)).groups()[0]
            filename_sw = hostname_sw + '.txt'
            file = open(filename_sw, 'w')
            print('正在获取的设备是:' + hostname_sw)
            file.write(telnet_get_config(host, i))
            file.close()
            print(e)


