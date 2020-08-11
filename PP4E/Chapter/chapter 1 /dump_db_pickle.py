#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import pickle

dbfile = open('people-file', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])