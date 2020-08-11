#!/bin/bash

# for 循环学习
#for i in `seq 1 15`
#
#do
#  echo -e "\033[32mthe number is $i\033[0m"  #
#done


# 求和,1-100
#j=0
#for ((i=1;i<=100;i++))
#
#do
#
#  j=`expr $i + $j`   # expr 表示求和， 使用示例：expr 12 + 13
#  # 1(i) + 0(j) = 1(j)
#  # 2(i) + 1(j) = 3(j)
#  # 3(i) + 3(j) = 6(j)
#
#done
#echo $j

# 示例代码

for i in `find /var/log -name "*.log" `
do
  tar -czvf 2014all.tgz $i
done
