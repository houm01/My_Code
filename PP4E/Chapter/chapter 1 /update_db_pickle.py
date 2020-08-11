#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import pickle


dbfile = open('people-file', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-file', 'wb')
pickle.dump(db, dbfile)
dbfile.close()