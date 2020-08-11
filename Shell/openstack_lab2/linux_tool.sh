#!/bin/bash

echo " =================<提示信息>================="
echo " 这是一个脚本工具箱，输入以下命令开始执行"
echo " 1）Linux 初始化，关闭 firewalld 和 Seliux"
echo " 2）修改网卡IP（CentOS）"   # 后面自动处理下 CentOS 与 ubuntu
echo " 3）打包 log 文件"
echo " 4）部署 OpenStack 练习环境，3 节点 kvm 虚拟机"
echo " ==========================================="


if [[ "$1" -eq "1" ]];then
  date
fi

if [[ "$1" -eq "2" ]];then
  ls /etc/sysconfig/network-scripts/ | grep ifcfg
fi
