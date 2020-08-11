#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import socket


def f1(request):
    """
    处理用户请求，并返回相应的内容

    """
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data


def f2(request):
    return b'f2'


routers = [
    ('/xxx', f1),
    ('/ooo', f2),
]


def run():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8090))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()

        data = conn.recv(8096)
        data = str(data, encoding='utf-8')  # 转换编码，并转换为字符串
        headers, bodys = data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')  # 分割请求头
        method, url, protocol = temp_list[0].split(' ')  # 拿到 method，url，protocol

        fuc_name = None
        for item in routers:
            if item[0] == url:
                fuc_name = item[1]
                break

        if fuc_name:
            response = fuc_name()
        else:
            response = b"404"

        conn.send(response)
        conn.close()


if __name__ == '__main__':
    run()

