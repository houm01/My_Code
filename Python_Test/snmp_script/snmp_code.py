#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmp_get_mem(ip, community, oid, port=161):
    errorIndication, errorStatus, errorindex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip,port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus,
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )

    result = ""
    for varBind in varBinds:
        result = result + varBind.prettyPrint()

    return result.split("=")[1].strip()


def snmpv2_getnext(ip, community, oid, port=161):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData(community),  # 设置community
        cmdgen.UdpTransportTarget((ip, port)),  # 设置IP地址和端口号
        oid,  # 设置OID
    )
    # 错误处理
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for varBindTableRow in varBindTable:
        for item in varBindTableRow:
            result.append((item.prettyPrint().split("=")[1].strip()))
            # item.prettyPrint().split("=")[0].strip() 这个就不添加了
    return result


def snmpv2_getbulk(ip, community, oid, count=25, port=161):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData(community),  # 配置community
        cmdgen.UdpTransportTarget((ip, port)),  # 配置IP地址和端口号
        0, count,  # 0为non-repeaters 和  25为max-repetitions(一个数据包中最多25个条目，和显示无关)
        oid,  # OID
    )

    """
    non-repeaters介绍
    the number of objects that are only expected to return a single GETNEXT instance, not multiple instances. Managers \
    frequently request the value of sysUpTime and only want that instance plus a list of other objects.
    max-repetitions介绍
    the number of objects that should be returned for all the repeating OIDs. Agent's must truncate the list to \
    something shorter if it won't fit within the max-message size supported by the command generator or the agent.
    详细介绍
    https://www.webnms.com/snmp/help/snmpapi/snmpv3/snmp_operations/snmp_getbulk.html
    """
    # 错误处理
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for varBindTableRow in varBindTable:
        for item in varBindTableRow:
            result.append((item.prettyPrint().split("=")[0].strip(), item.prettyPrint().split("=")[1].strip()))
    return result


if __name__ == "__main__":
    print(snmpv2_getnext('10.1.1.254', 'comlan', '1.3.6.1.2.1.4.20.1.3', port=161))
    # for x, y in snmpv2_getnext("10.1.1.254", "comlan", "1.3.6.1.2.1.2.2.1.2", port=161):
    #     print(x, y)

    # 使用Linux解释器 & WIN解释器
    # 显示接口信息
    # print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161))
    # for x, y in snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161):
    #     print(x, y)
    # # 接口速率
    # print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.5", port=161))
    #
    # # 进接口字节数
    # print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.10", port=161))
    #
    # # 出接口字节数
    # print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.16", port=161))


# print(snmp_get_mem('10.1.1.254', 'comlan', '1.3.6.1.2.1.4.20.1.2', port=161))

# for x, y in snmpv2_getbulk("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", count=25, port=161):
#         print(x, y)
#     # 接口速率
#     print(snmpv2_getbulk("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.5", port=161))
#
#     # 进接口字节数
#     print(snmpv2_getbulk("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.10", port=161))
#
#     # 出接口字节数
#     print(snmpv2_getbulk("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.16", port=161))