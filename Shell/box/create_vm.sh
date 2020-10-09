#!/usr/bin/env bash

# define vars
BASE_OS_DIRS=/data/houmingming/vmfiles/base_os
HOSTNAME=$2
IP=$3

help()
{
  cat <<- EOF
  Desc: Create VM
  Usage: ./create_vm.sh
  Author: houmingming

  -h --help
  -v --version
  -n --name
  -i --ip
EOF
 exit 0
}

echo $1
echo $2
echo $3


if $1 == "centos7";then
  cp $BASE_OS_DIRS/centos77_base.qcow2 /data/houmingming/vmfiles/os/${HOSTNAME}.qcow2
  if [ ! -d "/tmp/guest_qcow2/" ]; then
    mkdir /tmp/guest_qcow2/
  fi
  umount /tmp/guest_qcow2
  guestmount -a /data/houmingming/vmfiles/os/${hostname}.qcow2 --rw -i /tmp/guest_qcow2/
  cat << EOF > /tmp/guest_qcow2/etc/hostname
${hostname}
EOF
  cat << EOF > /tmp/guest_qcow2/etc/sysconfig/network-scripts/ifcfg-eth0
TYPE=Ethernet
NAME=eth0
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=172.19.10.${ip}
NETMASK=255.255.255.0
GATEWAY=172.19.10.254
EOF
  umount /tmp/guest_qcow2/
  virt-install --hvm --name "hmm-${hostname}" --cpu host-passthrough \
--memory 16384 --vcpus=8 \
--disk /data/houmingming/vmfiles/openstack/${hostname}.qcow2 \
--network=network=hmm-ovsbr0,portgroup=VLAN10,model=virtio \
--network=network=hmm-ovsbr0,portgroup=VLAN11,model=virtio \
--network=network=hmm-ovsbr0,portgroup=VLAN12,model=virtio \
--network=network=hmm-ovsbr0,portgroup=VLAN13,model=virtio \
--network=network=hmm-ovsbr0,portgroup=TRUNK,model=virtio \
--os-type=linux \
--os-variant centos7.0 \
--graphics vnc,listen=0.0.0.0 \
--noautoconsole  --import
fi

