#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import psycopg2
from snmp_script import snmp_code


core_ip = '10.1.1.254'
community_pass = 'comlan'

ipaddress_vlan = []

ipaddress = snmp_code.snmpv2_getnext(core_ip, community_pass, '1.3.6.1.2.1.4.20.1.1', port=161)
vlan = snmp_code.snmpv2_getnext(core_ip, community_pass, '1.3.6.1.2.1.4.20.1.2', port=161)
netmask = snmp_code.snmpv2_getnext(core_ip, community_pass, '1.3.6.1.2.1.4.20.1.3', port=161)

for i in zip(ipaddress, netmask, vlan):   # zip 可解决并行循环的问题
    ipaddress_vlan.append(i)


def write_to_db():
    conn = psycopg2.connect(dbname="houm01db", user="houm01dbuser", password="packet@123", host="docker.houm01.com")
    cursor = conn.cursor()
    cursor.execute("truncate table app01_comlan_device_ip_vlan")
    for x in ipaddress_vlan:
        cursor.execute("INSERT INTO app01_comlan_device_ip_vlan (ip, netmask, vlan) VALUES (%s, %s, %s)", (x[0], x[1], x[2]))
    conn.commit()
    cursor.close()
    conn.close()


write_to_db()

