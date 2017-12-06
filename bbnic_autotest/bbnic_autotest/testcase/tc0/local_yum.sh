#!/bin/bash
echo 'mount -o loop xx.iso /hans/os1'
#mount -o loop xx.iso /hans/os1
echo 'setup the local yum source'
cp ./rhel7.repo /etc/yum.repos.d/
yum clean all
yum makecache
