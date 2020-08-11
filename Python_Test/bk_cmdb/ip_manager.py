#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


import requests
import json


url = 'http://paas.bk.tyun.cn:80/api/c/compapi/v2/cc/search_business/'

data = {
    'app_code': 'cc',
    'app_secret': 'xxxxxx',
    'bk_token': '37bf1449-ebdc-4281-b7b3-61351c254ce7',
}

response = requests.get(url, params=data)

print(response.url)

# print(response.text)

data_json = json.loads(response.text)

print(data_json)