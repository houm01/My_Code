# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import requests


url = 'http://httpbin.org/post'

parms = {
    'name1': 'value1',
    'name2': 'value2'
}

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

text = resp.text

print(text)