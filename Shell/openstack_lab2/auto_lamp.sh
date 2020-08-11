#!/bin/bash
# 自动安装LAMP环境

# httpd define path variable
H_FILES=httpd-2.4.38.tar.bz2
H_FILES_DIR=httpd-2.4.38
H_URL=http://mirrors.cnnic.cn/apache/httpd/
H_PREFIX=/usr/local/apache2/

M_FILES=mysql-5.5.20.tar.gz
M_FILES_DIR=mysql-5.5.20
M_URL=http://down1.chinaunix.net/distfiles/
M_PREFIX=/usr/local/mysql/


if [ -z "$1" ];then
  echo -e "请选择一个菜单"
  echo -e "1)编译安装apache服务器"
  echo -e "2)编译安装Mysql服务器"
  echo -e "3)编译安装PHP服务器"
  echo -e "4)配置index.php并启动LAMP服务"
  echo -e "usage: { /bin/sh $0 1|2|3|$|help}"
  exit
fi

if [[ "$1" -eq "1" ]];then
  wget -c $H_URL/$H_FILES &&tar -jxvf $H_FILES &&cd $H_FILES_DIR ;./configure --prefix=$H_PREFIX

  if [ $? -eq 0 ];then
    make && make install
    echo -e "this $H_FILES_DIR server install success"
  else
    echo -e "the $H_FILES_DIR server install Failed"
    exit
  fi
fi

# 安装mysql
if [[ "$1" -eq "2" ]];then
  wget -c $M_URL/$M_FILES &&tar -jxvf $M_FILES &&cd $M_FILES_DIR ;./configure --prefix=$M_PREFIX

  if [ $? -eq 0 ];then
    make && make install
    echo -e "this $H_FILES_DIR server install success"
  else
    echo -e "the $H_FILES_DIR server install Failed"
    exit
  fi
fi

