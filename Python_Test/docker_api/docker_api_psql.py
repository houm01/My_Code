#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

import docker


# 获取容器状态信息
def get_info(Containers_id):
    c1 = client.containers.get(Containers_id).attrs
    print(c1['Name'])
    CONTAINER_ID = c1['Id']
    IMAGE = c1['Image']
    CREATED = c1['Created']
    STATUS = c1['State']['Status']
    HostConfig_Binds = c1['HostConfig']['Binds']
    if HostConfig_Binds == None:   # 这个值可能为None，如果不处理，后边插入数据库会报错
        HostConfig_Binds = 'None'
    PortBindings = c1['HostConfig']['PortBindings']
    RestartPolicy = c1['HostConfig']['RestartPolicy']['Name']
    Name = c1['Name']
    return CONTAINER_ID, IMAGE, CREATED, STATUS, HostConfig_Binds, PortBindings, RestartPolicy, Name


# 清空数据库
def delete_db():
    import psycopg2
    conn = psycopg2.connect(dbname="houm01db", user="houm01dbuser", password="packet@123", host="docker.houm01.com")
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE app01_dockercontainerstatus;")
    conn.commit()
    cursor.close()
    conn.close()


# 更新数据库
def update_db():
    import psycopg2
    conn = psycopg2.connect(dbname="houm01db", user="houm01dbuser", password="packet@123", host="docker.houm01.com")
    cursor = conn.cursor()

    # cursor.execute("SELECT COUNT(*) FROM app01_dockercontainerstatus where container_id = (%s)", (get_info(x)[0],))
    # in_or_not_in = cursor.fetchall()[0][0]
    # if in_or_not_in == 0:
    #     print('is ok')
    # else:
    #     print('is not ok')

    cursor.execute("INSERT INTO app01_dockercontainerstatus "
                   "(container_id, image, created, status, hostconfig_binds, portbindings, restartpolicy, name)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (get_info(x)[0], get_info(x)[1], get_info(x)[2], get_info(x)[3],
                    get_info(x)[4][0], str(get_info(x)[5]), get_info(x)[6], get_info(x)[7]))
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    client = docker.DockerClient(base_url='tcp://docker.houm01.com:4243')
    docker_ps = client.containers.list()
    delete_db()
    for i in docker_ps:
        x = str(i)[12:-1]
        update_db()





