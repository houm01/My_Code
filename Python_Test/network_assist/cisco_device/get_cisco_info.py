#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from netmiko import Netmiko


username = input("输入用户名:")
password = input("输入密码:")
enable_pass = input("输入enable密码:")
print(username, password, enable_pass)


def get_device_list():
    device_list = open('device_list.txt').read().splitlines()
    return device_list


def get_cisco_info(device_ip):
    my_device = {
        "host": device_ip,
        "username": username,
        "password": password,
        "secret": enable_pass,
        "device_type": "cisco_ios",
    }

    net_connect = Netmiko(**my_device)
    net_connect.enable()

    # 待优化命令输入方式
    version = net_connect.send_command('show version')
    cpu = net_connect.send_command('show proc cpu')
    cpu_history = net_connect.send_command('show proc cpu')
    memery = net_connect.send_command('show proc mem')
    file_system = net_connect.send_command('show file system')
    port_channel = net_connect.send_command('show etherchannel summary')
    vss = net_connect.send_command('show switch detail')
    ip_int_brief = net_connect.send_command('show ip int br')
    log = net_connect.send_command('show log')
    running_config = net_connect.send_command('show run')

    return '\n\n======show version======\n\n', version, \
           '\n\n======show proc cpu======\n\n', cpu,  \
           '\n\n======show cpu history======\n\n', cpu_history, \
           '\n\n======show memery======\n\n', memery, \
           '\n\n======show file system======\n\n', file_system, \
           '\n\n======show etherchannel summary======\n\n', port_channel, \
           '\n\n======show switch detail======\n\n', vss, \
           '\n\n======show ip int br======\n\n', ip_int_brief, \
           '\n\n======show logging======\n\n', log, \
           '\n\n======show running config======\n\n', running_config


if __name__ == '__main__':
    for i in get_device_list():
        fo = open("{}.txt".format(i), 'w+')
        fo.write(''.join(get_cisco_info(i)))
        fo.close()

