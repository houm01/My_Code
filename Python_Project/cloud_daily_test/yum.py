#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

# from bs4 import BeautifulSoup
from lxml import etree
import pymongo
import hashlib


question_answer_list = []


def parse_file():
    parser = etree.HTMLParser(encoding="utf-8")
    html_element = etree.parse('html/云服务能力每日一测61.htm', parser=parser)
    html = html_element.xpath("//div[@class='exam-question']")
    html_j = html_element.xpath("//div[@class='answers']")
    html_k = html_element.xpath("//div[@class='analysis-content question-ans-right']")

    for i, j, k in zip(html, html_j, html_k):
        pp = i.xpath("text()")[1].strip()
        jj = j.xpath("./div/label/span[@class='words']/text()")
        kk = k.xpath("text()")

        question_answer = {}

        pattern = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G':6 , '正': 0, '确': 0, '错': 1, '误': 1}
        rep = [pattern[x] if x in pattern else x for x in list(kk[0])]
        print(rep)
        if len(rep) == 1:
            question_answer['_id'] = hashlib.md5(pp.encode('utf8')).hexdigest()
            question_answer[pp.replace(".", "-")] = jj[rep[0]]
        elif len(rep) == 2:
            question_answer['_id'] = hashlib.md5(pp.encode('utf8')).hexdigest()
            question_answer[pp.replace(".", "-")] = jj[rep[0]], jj[rep[1]]
        elif len(rep) == 3:
            question_answer['_id'] = hashlib.md5(pp.encode('utf8')).hexdigest()
            question_answer[pp.replace(".", "-")] = jj[rep[0]], jj[rep[1]], jj[rep[2]]
        elif len(rep) == 4:
            question_answer['_id'] = hashlib.md5(pp.encode('utf8')).hexdigest()
            question_answer[pp.replace(".", "-")] = jj[rep[0]], jj[rep[1]], jj[rep[2]], jj[rep[3]]
        elif len(rep) == 5:
            question_answer['_id'] = hashlib.md5(pp.encode('utf8')).hexdigest()
            question_answer[pp.replace(".", "-")] = jj[rep[0]], jj[rep[1]], jj[rep[2]], jj[rep[3]], jj[rep[4]]
        else:
            pass
        question_answer_list.append(question_answer)

parse_file()


def insert_mongodb():
    my_client = pymongo.MongoClient("mongodb://10.20.99.106:27017")
    my_db = my_client["cloud_server"]
    my_col = my_db["sites5"]
    for i in question_answer_list:
        try:
            my_col.insert_one(i)
        except pymongo.errors.DuplicateKeyError:
            pass


insert_mongodb()

