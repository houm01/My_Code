#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from initdata import tom
import shelve


db = shelve.open('pepple-shelve')
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue
db['tom'] = tom
db.close()

