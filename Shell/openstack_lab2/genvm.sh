#!/bin/bash
vmname=$1
ip=$2

cp /data/vmfiles/tpl/centos77.qcow2 /data/vmfiles/openstack/${vmname}.qcow2

umount /tmp/vmtmp
[ -d /tmp/vmtmp ] || mkdir -pv /tmp/vmtmp
guestmount -a /data/vmfiles/openstack/${vmname}

sed -i "s@tmp/vmtmp/etc/xxxxxx@\$ip@g"

umount /tmp/vmtmp

 virt-install --name ${vmname} --memory 4096 --vcpus 2 --os-variant centos7.0 --disk /data/vmfiles/openstack/${vmname}.qcow2 --network=network=ovs-os3,portgroup=VLAN20 --network=network=ovs-os3,portgroup=VLAN21 --network=network=ovs-os3,portgroup=VLAN22 --network=network=ovs-os3,portgroup=VLAN23 --network=network=ovs-os3,portgroup=VLAN24 --network=network=ovs-os3,portgroup=TRUNK --graphics none --import
