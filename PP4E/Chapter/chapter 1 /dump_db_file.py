#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from make_db_file import LoadDbase, storeDbase


db = LoadDbase()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
