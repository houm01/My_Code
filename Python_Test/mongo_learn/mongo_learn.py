#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import pymongo


my_client = pymongo.MongoClient('mongodb://10.20.99.106:27017/')

db_list = my_client.list_database_names()

print(db_list)

