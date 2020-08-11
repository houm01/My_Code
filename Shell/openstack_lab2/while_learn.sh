#!/bin/bash

#i=1;
#while [[ $i -lt 10 ]];do
#    echo "This number is $i"
#    ((i++))
#done


# 逐行读取/etc/hosts的内容
while read line
do
  echo $line
done < /etc/hosts

