#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import openpyxl
from sqlalchemy import Column, String, create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


wb = openpyxl.load_workbook('/Users/houmingming/Library/Mobile Documents/com~apple~CloudDocs/项目/设备密码表-bak.xlsx')

active_sheet = wb.active

for row in active_sheet.values:
    pass
    # print(row)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    test = Column(String(30))




# Base.metadata.create_all(engine)

engine = create_engine('postgresql+psycopg2://houm01:packet123@box.tyun.cn/flask_db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)

new_user = User(id='5', name='Bob', test='demo')
session.add(new_user)
session.commit()
session.close()