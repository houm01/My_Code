#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

"""
用自定义格式将内存数据库对象保存到文件中
假定数据不使用 'endrec.', 'enddb.' 和 '=>'
假定数据库是字典的字典
...
翻译的有些看不懂，不抄了
"""

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    "将数据库格式化保存为普通文件"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name, RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def LoadDbase(dbfilename=dbfilename):
    "解析数据，重新构建数据库"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
