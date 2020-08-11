#!/bin/bash

BAK_DIR=/data/backup/`date +%Y%m%d`
MYSQLDB=mysql
MYSQLUSR=root
MYSQLPW=packet123
MYSQLCMD=/usr/bin/mysqldump

if [ $UID -ne 0 ];then   # 判断当前用户是否为root
  echo "must to be use root"
  exit
fi

if [ ! -d $BAK_DIR ];then
  mkdir -p $BAK_DIR
  echo "[32mThe $BAK_DIR create success]"
else
  echo "this $BAK_DIR is exists..."
fi

$MYSQLCMD -u$MYSQLUSR -p$MYSQLPW $MYSQLDB >$BAK_DIR/$MYSQLDB.sql

if [ $? -eq 0 ];then
  echo -e "the mysql backup $MYSQLDB success"
else
  echo -e "backup $MYSQLDB failed, please check"
fi