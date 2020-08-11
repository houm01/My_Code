#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from initdata import bob, sue, tom
import pickle

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()

