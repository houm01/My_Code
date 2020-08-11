#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import pickle, glob
for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])

