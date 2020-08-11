#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)


bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())