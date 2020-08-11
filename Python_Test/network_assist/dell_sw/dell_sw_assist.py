#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com

import os
import re


def get_dell_sw_info(raw_info):
    with open(raw_info, 'r') as f:
        raw_text = f.read()
        hostname = re.search('hostname (.*)', raw_text).groups()[0]
        mgt_ip = re.search('interface ManagementEthernet (.*)\n ip address (.*)/(.*)', raw_text).groups()[1]
        model = re.search('System Type: (.*)', raw_text).groups()[0]
        version = re.search('Dell Application Software Version:  (.*)', raw_text).groups()[0]
        uptime = re.search('Dell Networking OS uptime is (.*)', raw_text).groups()[0]
        try:
            cpu_usage = re.search('Overall      (.*)           (.*)            (.*)', raw_text).groups()[2]
        except AttributeError:
            cpu_usage = 'cpu is 0%'
        memory_total = re.search('Total:  (.*), MaxUs', raw_text).groups()[0]
        memory_used = re.search('CurrentUsed:  (.*),', raw_text).groups()[0]
        memory_per = '%.2f%%' % (int(memory_used) / int(memory_total))

    print(hostname, mgt_ip, model, version, uptime, cpu_usage, memory_per)


if __name__ == '__main__':
    os.chdir('/Users/houmingming/tmp/Python assist')
    for x in os.listdir():
        if 'DS_S' not in x:
            get_dell_sw_info(x)
