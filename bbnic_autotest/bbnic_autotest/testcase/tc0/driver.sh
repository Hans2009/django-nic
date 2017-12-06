#!/bin/bash
echo 'Installation automatically for driver'
echo '1.Install RPMs'
echo '2.Install driver'
source install.sh 
./INSTALL -a 
reboot
