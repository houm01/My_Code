#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'cookie': '_csrf=xMpBybTkwEz94KqcgEmHEIsW; deviceId=1045a67e-fb10-46bf-b80c-61ce9f7148a2; deviceIdGenerateTime=1569486992188; shimo_gatedlaunch=2; shimo_kong=7; shimo_svc_edit=5843; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; intercom-id-o2orsbzq=336af08b-2634-4f88-b789-45f718114040; anonymousUser=-2530327842; shimo_sid=s%3Anj4R9DPmXlS-Id8tHU_w8oHtJOCBRSDW.94GoyDTImptAxQCAnB2%2BOVWES86Ezh%2B%2F3f7sSuk1qEo; rememberMeToken=oC9Y9G3jSMgMP11U; ignore_this_cookies=nothing; userId=20061701; login_referer=; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2220061701%22%2C%22%24device_id%22%3A%2216d6cb6f3aa1b3-0bcdc859119c65-396a4507-2073600-16d6cb6f3ab7a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216d6cb6f3aa1b3-0bcdc859119c65-396a4507-2073600-16d6cb6f3ab7a%22%7D; locale=zh-CN',
}

url = 'https://shimo.im/desktop'
session = requests.Session()
response = session.get('https://shimo.im/desktop', headers=headers)

print(response.status_code)
print(response.text)
