#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import json
import sys


headers = {'Content-Type': 'application/json;charset=utf-8'}

# 填写你的 api url
api_url = "https://oapi.dingtalk.com/robot/send?access_token=3c5f91df1cf65a8d5b068c6dbbfce30b98c3f35388b3ef9e713ce0b1b72d6c65"


def msg(text):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                "1xxxxxxxxxxxxx"
            ],
            "isAtAll": False
        }
    }
    # 注意这里是为了没有下滑线的提示才将 print 改为了 python3 的形式，使用时务必改回去，也就是不要括号
    # print requests.post(api_url, json.dumps(json_text), headers=headers).content
    requests.post(api_url, json.dumps(json_text, headers=headers)).content


if __name__ == '__main__':
    text = '123test'
    msg(text)

