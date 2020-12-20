#!/bin/bash

hostname=$1
ip=$2

cp /data/houmingming/vmfiles/base_os/centos82_base.qcow2 /data/houmingming/vmfiles/os/hostname_vm.qcow2

export LIBGUESTFS_BACKEND=direct

if [ ! -d "/tmp/guest_qcow2/" ]; then
    mkdir /tmp/guest_qcow2/
fi

# 清掉现有的挂载点
umount /tmp/guest_qcow2

# 挂载，目前是要修改IP地址和主机名
guestmount -a /data/houmingming/vmfiles/os/hostname_vm.qcow2 --rw -i /tmp/guest_qcow2/

# 更改hostname
cat << EOF > /tmp/guest_qcow2/etc/hostname
hostname_vm
EOF

# 更改管理网络的IP地址
cat << EOF > /tmp/guest_qcow2/etc/sysconfig/network-scripts/ifcfg-ens3
TYPE=Ethernet
NAME=ens3
DEVICE=ens3
BOOTPROTO=static
ONBOOT=yes
IPADDR=172.19.10.ip
NETMASK=255.255.255.0
GATEWAY=172.19.10.254
EOF

# 取消挂载
umount /tmp/guest_qcow2/

# 安装虚拟机
virt-install --hvm --name "hostname_vm" --cpu host-passthrough \
--memory 16384 --vcpus=8 \
--disk /data/houmingming/vmfiles/os/hostname_vm.qcow2 \
--network=network=ovsbr0,portgroup=VLAN10,model=virtio \
--network=network=ovsbr0,portgroup=VLAN11,model=virtio \
--network=network=ovsbr0,portgroup=VLAN12,model=virtio \
--network=network=ovsbr0,portgroup=VLAN13,model=virtio \
--network=network=ovsbr0,portgroup=TRUNK,model=virtio \
--os-type=linux \
--graphics vnc,listen=0.0.0.0 \
--noautoconsole  --import