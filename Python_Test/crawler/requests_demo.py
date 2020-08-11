#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import requests
import selenium

# headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/76.0.3809.132 Safari/537.36',
#            }
#
# response = requests.get('www.baidu.com', headers=headers)
#
# # print(response.text)  # 所有的响应信息
# # print(response.headers)  # 字典形式结构
# # print(response.status_code)
# # print(response.content)  # 二进制的形式
#
# requests.request('GET', 'http://www.baidu.com', data=kv)

# params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
#
# r = requests.post("http://pythonscraping.com/pages/processing.php", data=params)
#
# print(r.text)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)',
}
url = 'https://www.kaoshixing.com/login/account/login'

data = {"userName": "houmingming@90241",
        "userNameInput": "houmingming",
        "companyId": "90241",
        "newCompanyId": "90241",
        "password": "TyuN@!#123"}
session = requests.Session()
session.post(url, data=data,headers=headers)
response = session.get('https://exam.kaoshixing.com/exam/')

print(response.status_code)
print(response.text)