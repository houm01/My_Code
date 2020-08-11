#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com

from netmiko import Netmiko

username = input("请输入用户名：")
password = input("请输入密码")

print(username, password)


def get_device_list():
    device_list = open('device_list.txt').read().splitlines()
    return device_list


def get_hw_esn(device_ip):
    my_device = {
        "host": device_ip,
        "username": username,
        "password": password,
        "device_type": "huawei",
    }

    net_connect = Netmiko(**my_device)

    hw_esn = net_connect.send_command('display esn')

    print(device_ip, ":", hw_esn)


if __name__ == '__main__':
    for i in get_device_list():
        get_hw_esn(i)
