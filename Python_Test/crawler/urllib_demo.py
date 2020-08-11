#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

# import urllib.request
#
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('utf-8'))   # 这里得到的结果并不完整，但视频中显示的是完整的


# import urllib.parse
# import urllib.request
#
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())


# import urllib.request
#
# response = urllib.request.urlopen('http://py.houm01.com:3000/get', timeout=10)
# print(response.read())

# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://py.houm01.com:3000/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# import urllib.request
#
# response = urllib.request.urlopen('http://py.houm01.com:3000')
# print(type(response))


# import urllib.request
#
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


import urllib.request

request = urllib.request.Request('http://py.houm01.com:3000')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))