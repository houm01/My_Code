#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com


import json
import xmltodict
import psycopg2
import os


def xml_to_json(xml_str):
    xmlparse = xmltodict.parse(xml_str)
    jsonstr = json.dumps(xmlparse, indent=1)
    return jsonstr


def get_address_book():
    finnal_address_list = []
    os.chdir('/Users/houmingming/cache')
    with open('test.xml') as file:
        j = json.loads(xml_to_json(file.read()))

    address_book_raw = j['rpc-reply']['configuration']['security']['address-book']

    for x in address_book_raw['address']:
        try:
            finnal_address_list.append([address_book_raw['name'], x['name'], x['ip-prefix'], 'ip-prefix'])
        except KeyError:
            finnal_address_list.append([address_book_raw['name'], x['name'], x['dns-name']['name'], 'dns-name'])

    address_book_set = address_book_raw['address-set']
    for x in address_book_set:
        for i in x['address']:
            for y in finnal_address_list:
                if i['name'] == y[1]:
                    y.insert(1, x['name'])

    for x in finnal_address_list:
        if len(x) == 4:
            x.insert(1, 'None')

    return finnal_address_list


def get_address_set():
    os.chdir('/Users/houmingming/cache')
    with open('test.xml') as file:
        j = json.loads(xml_to_json(file.read()))

    address_book_raw = j['rpc-reply']['configuration']['security']['address-book']['address-set']

    finally_address_set = []

    for x in address_book_raw:
        for i in x['address']:
            # print(i['name'])
            finally_address_set.append([x['name'], i['name']])
    return finally_address_set


def create_worksheet():
    with open('srx345_config_xml') as file:
        j = json.loads(xml_to_json(file.read()))

    sheet_test = []

    for value in j['rpc-reply']['configuration']['security']['policies']['policy']:
        if isinstance(value['policy'], list):    # 如果是 list，说明该区域有多条策略

            aa = len(value['policy'])   # 使用aa和bb保证策略不乱序
            bb = 0

            while bb < aa:
                try:
                    sheet_test.append((value['from-zone-name'],value['to-zone-name'],
                                       value['policy'][bb]['name'],
                                       "{}: {}".format(value['policy'][bb]['match']['source-address'], get_address_book()[value['policy'][bb]['match']['source-address']]),
                                       "{}: {}".format(value['policy'][bb]['match']['destination-address'], get_address_book()[value['policy'][bb]['match']['destination-address']]),
                                       value['policy'][bb]['match']['application'],
                                       value['policy'][bb]['then']
                                       ))

                except TypeError:
                    for single_src_add in value['policy'][bb]['match']['source-address']:
                        pass

                finally:
                    bb += 1

        else:    # 如果是 dict，说明该区域只有一条策略
            try:
                sheet_test.append((value['from-zone-name'],
                                   value['to-zone-name'],
                                   value['policy']['name'],
                                   get_address_book()[value['policy']['match']['source-address']],
                                   get_address_book()[value['policy']['match']['destination-address']],
                                   value['policy']['match']['application'],
                                   value['policy']['then']))
            except TypeError:
                list1 = []
                for x in value['policy']['match']['source-address']:
                    list1.append("{}: {}".format(x, Get_address_book()[x]))
                # print(''.join(str(list1)))

                list2 = []
                print(value['policy']['match']['destination-address'])
                print(list2)

                sheet_test.append((value['from-zone-name'],
                                   value['to-zone-name'],
                                   value['policy']['name'],
                                   str(list1),
                                   value['policy']['match']['destination-address'],
                                   value['policy']['match']['application'],
                                   value['policy']['then']))
    print(sheet_test)


def policy_analysis():
    os.chdir('/Users/houmingming/cache')
    with open('test.xml') as file:
        j = json.loads(xml_to_json(file.read()))

    finally_policy = []

    for value in j['rpc-reply']['configuration']['security']['policies']['policy']:
        for x in value['policy']:
            for i in x['then'].keys():
                finally_policy.append([value['from-zone-name'], value['to-zone-name'], x['name'], x['match']['source-address'], x['match']['destination-address'], i])

    return finally_policy


def write_to_db():
    conn = psycopg2.connect(dbname="python_public_db", user="python_public_user", password="python_public_pass", host="10.1.1.16")
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists example_srx_345_address_book "  
                "(name varchar,"
                "address_book varchar,"
                "address varchar,"
                "type varchar);")

    for x in get_address_book():
        cur.execute("INSERT INTO example_srx_345_address_book (name, address_book,address,type )"
                    "VALUES (%s, %s, %s, %s)", (x[0], x[2], x[3], x[4]))

    cur.execute("CREATE TABLE if not exists example_srx_345_address_set "
                "(address_set varchar,"
                "address_book_name varchar);")

    for y in get_address_set():
        cur.execute("INSERT INTO example_srx_345_address_set (address_set, address_book_name )"
                    "VALUES (%s, %s)", (y[0], y[1]))

    cur.execute("CREATE TABLE if not exists example_srx_345_policy "
                "(from_zone varchar ,"
                "to_zone varchar,"
                "policy_name varchar,"
                "source_address varchar,"
                "destination_address varchar,"
                "action varchar);")

    for i in policy_analysis():
        if i[3] is list and i[4] is list:
            a = ','.join(i[3])
            b = ','.join(i[4])
            cur.execute("INSERT INTO example_srx_345_policy (from_zone, to_zone, policy_name, source_address, destination_address, action )"
                        "VALUES (%s, %s, %s, %s, %s, %s)", (i[0], i[1], i[2], a, b, i[5]))
        elif i[3] is list and i[4] is not list:
            a = ','.join(i[3])
            cur.execute("INSERT INTO example_srx_345_policy (from_zone, to_zone, policy_name, source_address, destination_address, action )"
                        "VALUES (%s, %s, %s, %s, %s, %s)", (i[0], i[1], i[2], a, i[4], i[5]))
        elif i[4] is list and i[3] is not list:
            b = ','.join(i[4])
            cur.execute(
                "INSERT INTO example_srx_345_policy (from_zone, to_zone, policy_name, source_address, destination_address, action )"
                "VALUES (%s, %s, %s, %s, %s, %s)", (i[0], i[1], i[2], i[3], b, i[5]))
        else:
            cur.execute(
                "INSERT INTO example_srx_345_policy (from_zone, to_zone, policy_name, source_address, destination_address, action )"
                "VALUES (%s, %s, %s, %s, %s, %s)", (i[0], i[1], i[2], i[3], i[4], i[5]))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    # policy_analysis()
    # write_to_db()
    # get_address_set()
    write_to_db()







