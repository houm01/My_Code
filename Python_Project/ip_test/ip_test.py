#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


import os
import smtplib
import datetime
import psycopg2
from pypinyin import lazy_pinyin
from email.utils import formataddr
from email.mime.text import MIMEText

# 定义一个邮件的列表
mail_down_ip_body = []


# 操作IP数据库，测试不通的设置为 is down
def ping_ip():
    # 用 os.system ping 太慢了，可以优化一下，使用 python 封装 icmp，并使用多线程
    conn = psycopg2.connect(dbname="houm01db", user="postgres", password="packet123", host="10.20.99.105", port="5432")
    cursor = conn.cursor()

    # 操作前备份一下table，防止自己网络有问题，将所有ip都设为down状态了
    # cursor.execute("select china_edu from ip_test;")
    # ip_list_edu = cursor.fetchall()
    # for i in ip_list_edu:
    #     response = os.system('ping -c 8 ' + i[0])
    #     if response == 0:
    #         print(i[0], 'is up')
    #     else:
    #         print(i[0], 'is down')
    #         cursor.execute("update ip_test set china_edu = 'is down' where china_edu = (%s) and china_edu != 'is down';", (i[0],))
    #         cursor.execute("select state, city from ip_test where china_edu = (%s);",
    #                        (i[0],))
    #         china_edu_down_name = cursor.fetchall()
    #         for z in china_edu_down_name:
    #             mail_down_ip_body.append(('教育网', z[0].rstrip() + z[1].rstrip(), i[0].rstrip()))

    # 为节省时间，这里就不合并到一起了
    cursor.execute("select china_unicom from ip_test;")
    ip_list_unicom = cursor.fetchall()
    for i in ip_list_unicom:
        response = os.system('ping -c 8 ' + i[0])
        if response == 0:
            print(i[0], 'is up')
        else:
            print(i[0], 'is down')
            cursor.execute("select state, city from ip_test where china_unicom = (%s) and china_unicom != 'is down';",
                           (i[0],))
            china_unicom_down_name = cursor.fetchall()
            for z in china_unicom_down_name:
                mail_down_ip_body.append(('联通', z[0].rstrip() + z[1].rstrip(), i[0].rstrip()))
            cursor.execute("update ip_test set china_unicom = 'is down' where china_unicom = (%s);",
                           (i[0],))

    cursor.execute("select china_mobile from ip_test;")
    ip_list_mobile = cursor.fetchall()
    for i in ip_list_mobile:
        response = os.system('ping -c 8 ' + i[0])
        if response == 0:
            print(i[0], 'is up')
        else:
            print(i[0], 'is down')
            cursor.execute("select state, city from ip_test where china_mobile = (%s) and china_mobile != 'is down';",
                           (i[0],))
            china_mobile_down_name = cursor.fetchall()
            for z in china_mobile_down_name:
                mail_down_ip_body.append(('移动', z[0].rstrip() + z[1].rstrip(), i[0].rstrip()))
            cursor.execute("update ip_test set china_mobile = 'is down' where china_mobile = (%s);",
                           (i[0],))

    cursor.execute("select china_telecom from ip_test;")
    ip_list_telecom = cursor.fetchall()
    for i in ip_list_telecom:
        response = os.system('ping -c 8 ' + i[0])
        if response == 0:
            print(i[0], 'is up')
        else:
            print(i[0], 'is down')
            cursor.execute("select state, city from ip_test where china_telecom = (%s) and china_telecom != 'is down';",
                           (i[0],))
            china_telecom_down_name = cursor.fetchall()
            for z in china_telecom_down_name:
                mail_down_ip_body.append(('电信', z[0].rstrip() + z[1].rstrip(), i[0].rstrip()))
            cursor.execute("update ip_test set china_telecom = 'is down' where china_telecom = (%s);",
                           (i[0],))

    cursor.execute("select ip from ip_test_international;")
    ip_list_int = cursor.fetchall()
    for i in ip_list_int:
        response = os.system('ping -c 8 ' + i[0])
        if response == 0:
            print(i[0], 'is up')
        else:
            print(i[0], 'is down')
            cursor.execute("select name from ip_test_international where ip = (%s) and ip != 'is down';",
                           (i[0],))
            ip_int_down_name = cursor.fetchall()
            try:
                mail_down_ip_body.append((ip_int_down_name[0][0], i[0]))
            except IndexError:
                pass
            cursor.execute("update ip_test_international set ip = 'is down' where ip = (%s);",
                           (i[0],))

    conn.commit()
    cursor.close()
    conn.close()


# 从数据库拿到国内和国际的IP测试数据
def get_data():
    conn = psycopg2.connect(dbname="houm01db", user="postgres", password="packet123", host="10.20.99.105", port="5432")
    cursor = conn.cursor()
    cursor.execute("select state, city, china_telecom, china_unicom, china_mobile, china_edu from ip_test;")
    ip_test = cursor.fetchall()
    cursor.execute("select name, name_en, ip from ip_test_international;")
    ip_test_int = cursor.fetchall()
    cursor.close()
    conn.close()
    return ip_test, ip_test_int


def output_config():
    china_telcom = []
    china_unicom = []
    china_mobile = []
    int_ip = []
    for i in get_data()[0]:
        if 'is down' != (i[2].rstrip()):
            china_telcom.append(('+++ dianxin-' + ''.join(x[0] for x in lazy_pinyin(i[0].rstrip().rstrip('市'))) + '-' + str(i[2]).replace('.', ''), 'menu = ' + i[0].rstrip().rstrip('市') + i[1].rstrip().rstrip('市') + '电信', 'title = ' + ''.join(lazy_pinyin(i[0].rstrip().rstrip('市'))) + '-' + ''.join(lazy_pinyin(i[1].rstrip().rstrip('市'))) + '-' + i[2].rstrip(), 'host = ' + i[2].rstrip()))

    for i in get_data()[0]:
        # print(i[3].rstrip())
        if 'is down' != (i[3].rstrip()):
            china_unicom.append(('+++ liantong-' + ''.join(x[0] for x in lazy_pinyin(i[0].rstrip().rstrip('市'))) + '-' + str(i[3]).replace('.', ''), 'menu = ' + i[0].rstrip().rstrip('市') + i[1].rstrip().rstrip('市') + '联通', 'title = ' + ''.join(lazy_pinyin(i[0].rstrip().rstrip('市'))) + '-' + ''.join(lazy_pinyin(i[1].rstrip().rstrip('市'))) + '-' + i[3].rstrip(), 'host = ' + i[3].rstrip()))

    for i in get_data()[0]:
        if 'is down' != (i[4].rstrip()):
            china_mobile.append(('+++ yidong-' + ''.join(x[0] for x in lazy_pinyin(i[0].rstrip().rstrip('市'))) + '-' + str(i[4]).replace('.', ''), 'menu = ' + i[0].rstrip().rstrip('市') + i[1].rstrip().rstrip('市') + '移动', 'title = ' + ''.join(lazy_pinyin(i[0].rstrip().rstrip('市'))) + '-' + ''.join(lazy_pinyin(i[1].rstrip().rstrip('市'))) + '-' + i[4].rstrip(), 'host = ' + i[4].rstrip()))

    for i in get_data()[1]:
        if 'is down' != (i[2]):
            int_ip.append(('++ ' + ''.join(i[1]), 'menu = ' + i[0], 'title = ' + i[1] + '-' + i[2], 'host = ' + i[2]))

    return china_telcom, china_unicom, china_mobile, int_ip


# 将之前所有获取的信息整理成smokeping所需的"Targets"配置文件
# 这里变量设置的比较乱
def finally_target():
    with open('ip_target.txt', 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        with open('begin_text', 'r') as file:
            f.write(file.read() + '\n' + content)
            print(f.read())
    with open('ip_target.txt', 'a') as f:
        with open('end_text', 'r') as file:
            f.write(file.read())

    with open('ip_target.txt', 'r+') as f:
        aa = f.read()
        pos = aa.find('+++ liantong')
        cc = aa[:pos] + """
++ liantong #联通
menu = 联通网络监控 
title = China Unicom 
#host = /Other/liantong/liantong-bj /Other/liantong/liantong-sh       /Other/liantong/liantong-gz 
        """ + '\n' + aa[pos:]

        dd = cc.find('+++ yidong')
        ee = cc[:dd] + """
++ yidong #移动
menu = 移动网络监控 
title = China mobile
""" + '\n' + cc[dd:]

        ff = ee.find('++ Tokyo-Japan')
        gg = ee[:ff] + """
+ Internet
menu = 国际线路
title = 国际线路
        """ + '\n' + ee[ff:]

        with open('Targets', 'w') as finally_txt:
            finally_txt.write(gg)


def mail():
    my_sender = 'houm01@foxmail.com'
    my_user = 'houm01@foxmail.com'
    my_pass = 'vcqvmwgmwgzlbajb'

    with open('text.txt', 'w') as f:
        for i in mail_down_ip_body:
            f.write(str(i).replace('(', '').replace(')', '').replace('\'', '').replace(',', ' -- ') + '\n')

    with open('text.txt', 'r') as f:
        mail_txt_str = f.read()

    if len(mail_txt_str) != 0:
        mail_text = '''{} 检测到新增 down ip 如下\n\n{}\n已生成Targets文件，请管理员判断是否处理'''.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), mail_txt_str)
        scan_state = '有新增的down ip，请关注'
    else:
        mail_text = '''{} 经过检测，没有发现有新增down的IP\n
                {}
                '''.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), mail_txt_str)
        scan_state = '无新增down ip'

    ret = True
    try:
        msg = MIMEText(mail_text, 'plain', 'utf-8')
        msg['From'] = formataddr(["Smokeping 测试", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["Service", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "Smokeping 测试结果报告 - {} - {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), scan_state)  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")


if __name__ == '__main__':
    ping_ip()
    with open('ip_target.txt', 'w') as f:
        for i in output_config():
            for y in i:
                for z in y:
                    f.write(z + '\n')
    finally_target()

    mail()



