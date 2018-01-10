#!/bin/bash
echo 'Installation automatically for driver'
echo '1.Install RPMs'
cd /opa/pkg/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134/
#source install.sh
echo '2.Install driver'
./INSTALL -a
#reboot
