#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import shelve

db = shelve.open('class-shelve')
sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()

