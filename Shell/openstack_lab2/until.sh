#!/bin/bash

# 满足条件才退出
#a=10;
#until [[ $a -lt 0 ]]; do
#    echo $a;
#    ((a--));
#done

# case选择语句
#ps3="select your will exec menu"
#
#select i in "apache" "msql" *; do
#
#case $i in
#  apache)   # apache 和 select 中的内容是一一对应的
#  echo "wait install httpd server..."
#  tar jxvf httpd-2.4.38.tar.bz2;cd httpd-2.4.38
#  ;;
#
#  Mysql)
#     echo "wait install mysql server"
#  ;;
#esac
#
#done
# select 语句


# 数组练习
#soft=(
#    nginx-1.6.1.tar.gz
#    mysql-5.1.17.tar.gz
#    php-5.3.3.tar.gz
#    /etc/sysctl.conf
#)
#
#echo "This is soft total ${#soft[@]} !"
#
#tar -xzf ${soft[0]};cd nginx-1.6.1 ;./configure ;make ;make install


# 函数练习
#function command() {
#  xx.xx
#
#}
## 调用函数
#command


# 函数使用示例
NGX_FILES=nginx-1.6.1.tar.gz
NGX_SRC=`echo $NGX_FILES`|sed '\.tar\.gz//g'
DWN_URL=http://nginx.org/download/
MYSQL_FILES=mysql-5.1.17.tar.gz

function nginx_install() {
  wget -c ${DWN_URL}/${NGX_FILES}
  tar xzf $NGX_FILES ;cd nginx-1.6.1 ;//configure ;make ;make install
  if [ $? -eq 0 ];then
    echo "nginx install success"
  fi
}
function mysql_install() {

  tar zxf $MYSQL_FILES ;cd mysql-5.1.17 ;./configure --prefix=/usr/local/mysql ;make ;make install

}
function php_install() {
  if [ -d /usr/local/mysql ];then
  tar xzf $PHP_FILES ;cd php-5.3.3 ;./configure --prefix=/usr/local/php
  else
    echo "please pre install mysql"
  fi
}
