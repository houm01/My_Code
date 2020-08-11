#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from initdata import db
import pickle


dbfile = open('people-file', 'wb')
pickle.dump(db, dbfile)
dbfile.close()