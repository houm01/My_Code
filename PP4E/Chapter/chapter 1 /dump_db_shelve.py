#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import shelve


db = shelve.open('pepple-shelve')
for key in db:
    print(key, "=>", db[key])

print(db['sue']['name'])
db.close()