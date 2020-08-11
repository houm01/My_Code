#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from make_db_file import LoadDbase, storeDbase


db = LoadDbase()
db['sue']['pay '] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)