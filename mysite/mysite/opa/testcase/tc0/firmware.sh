#!/bin/bash
echo 'Installation automatically for firmware'
echo '1.Install RPMs'
echo '2.Install firmware' 
cd /usr/share/opa/bios_images/
ls -l
hfi1_eprom -w -o HfiPcieGen3Loader_*.rom -b HfiPcieGen3_*.efi -c /lib/firmware/updates/hfi1_platform.dat
hfi1_eprom -V -o
hfi1_eprom -V -b
hfi1_eprom -V -c
cd /lib/firmware/updates/
opatmmtool -f hfi1_smbus.fw fileversion
opatmmtool -f hfi1_smbus.fw update
opahfirev
