#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com


LIMIT = int(input("每个文件有多少行? 请输入:"))


file_count = 1
url_list = []


with open('u_ex190730-cas02.log') as f:
    for line in f:
        url_list.append(line)
        if len(url_list) < LIMIT:
            continue
        file_name = 'u_ex190730-cas02' + '-' + str(file_count) + ".txt"
        with open(file_name, 'w') as file:
            for url in url_list[:-1]:
                file.write(url)
            file.write(url_list[-1].strip())
            url_list = []
            file_count += 1

if url_list:
    file_name = str(file_count) + ".txt"
    with open(file_name, 'w') as file:
        for url in url_list:
            file.write(url)

print('done')
