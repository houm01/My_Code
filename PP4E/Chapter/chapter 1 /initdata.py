#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

# 也可以写成 db = {}，但是 Pycharm 有不规范的提示，如下
# This dictionary creation could be rewritten as a dictionary literal
db = dict()
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


if __name__ == '__main__':
    for key in db:
        print(key, '=>', db[key])
