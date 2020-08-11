#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from notion.client import NotionClient


client = NotionClient(token_v2='3e284b134914d90ddd1f1c98a0b22d0876db01a1d78ab7573af90b51a0426ae8873b37aa64204ebff0e56ba17247f1415ee875b048cc591ab9ee7dec88a0711a1f423e8a5c32c4f78d14')

page = client.get_block("https://www.notion.so/htest-429be1ef2ee82oum01/d8c022b167")

print(page.title)

