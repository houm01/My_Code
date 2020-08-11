#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from initdata import bob, sue
import shelve


db = shelve.open('pepple-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()

