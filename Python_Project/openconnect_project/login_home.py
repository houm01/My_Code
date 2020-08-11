#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import pexpect
import configparser
import requests
import json
import os
import time


# 获取配置文件中的内容
config = configparser.ConfigParser()
config.read('/data/config_dir/home_vpn_config.ini')

VPN_Server = config.get('VPN_Server', 'url')
Username = config.get('Auth', 'Username')
Password = config.get('Auth', 'Password')
api_url = config.get('url', 'api_url')
test_ip = config.get('VPN_Server', 'test_ip')

def login_ssl_vpn():
    # 尝试登录,screen 表示新生成一个窗口，要不程序执行完后，就又断了
    child = pexpect.spawn('screen openconnect {} --no-dtls'.format(VPN_Server))

    child.expect('else to view')
    child.sendline('yes')

    child.expect('OperationsUser')
    child.sendline('GuestUser')

    child.expect('Username')
    child.sendline(Username)

    child.expect('Password')
    child.sendline(Password)
    child.sendline('\01d')

    time.sleep(5)


def info_get():
# 信息获取
#     route_table = os.popen("route -n").read()
    inet_enp6s0 = os.popen("ip add show enp6s0 | grep inet | awk '{print $2}' | grep -v ':'").read()
    inet_tun0 = os.popen("ip add show tun0 | grep inet | awk '{print $2}' | grep -v ':'").read()

    service_openvswitch = os.popen("systemctl status openvswitch-switch.service | grep Active | awk '{print $2}'").read()
    service_libvirtd = os.popen("systemctl status libvirtd | grep Active | awk '{print $2}'").read()

    return inet_enp6s0, inet_tun0, service_openvswitch, service_libvirtd


def msg():
    # dingtalk notification
    headers = {'Content-Type': 'application/json;charset=utf-8'}

    json_text= {
     "msgtype": "markdown",
     "markdown": {
          "title": "开机状态确认",
            "text": "## 开机状态确认\n "
                    "******************\n"
                    "### IP地址 \n "
                    "- **enp6s0**: {}\n"
                    "- **tun0**: {}\n"
                    "******************\n"
                    "### 服务状态\n"
                    "- **openvswitch**: {}"
                    "- **libvirtd**: {}".format(info_get()[0], info_get()[1], info_get()[2], info_get()[3])
        },
        "at": {
            "atMobiles": [
                "18500087233"
            ],
            "isAtAll": False
        }
    }

    requests.post(api_url, json.dumps(json_text), headers=headers).content


if __name__ == '__main__':
    ping_result = os.popen("ping -c 3 {} | grep '0 received' | wc -l".format(test_ip)).read()
    if int(ping_result) == 1:
        login_ssl_vpn()
        msg()
    else:
        pass
