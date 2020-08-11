#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


import psycopg2

conn = psycopg2.connect(dbname="houm01db", user="houm01dbuser", password="packet@123", host="docker.houm01.com")
cursor = conn.cursor()
cursor.execute("select id,tittle from classes;")
class_list = cursor.fetchall()
print(class_list)
cursor.close()
conn.close()