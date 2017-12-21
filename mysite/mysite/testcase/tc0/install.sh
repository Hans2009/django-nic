#!/bin/bash
#This is for redhat 7.4
yum install -y --nogpgcheck rdma-core
yum install -y --nogpgcheck opensm-libs
yum install -y --nogpgcheck libibmad
yum install -y --nogpgcheck libibcm
yum install -y --nogpgcheck libibumad
yum install -y --nogpgcheck rdma-core-devel
yum install -y --nogpgcheck tcsh
yum install -y --nogpgcheck libibverbs
yum install -y --nogpgcheck ibacm
yum install -y --nogpgcheck atlas
yum install -y --nogpgcheck bc
yum install -y --nogpgcheck expect
yum install -y --nogpgcheck tcl
yum install -y --nogpgcheck qperf
yum install -y --nogpgcheck perftest
yum install -y --nogpgcheck infinipath-psm
yum install -y --nogpgcheck libgfortran
yum install -y --nogpgcheck gcc-gfortran
yum install -y --nogpgcheck libquadmath
yum install -y --nogpgcheck librdmacm
yum install -y --nogpgcheck libstdc++-devel
yum install -y --nogpgcheck papi
yum install -y --nogpgcheck elfutils-libelf-devel
yum install -y --nogpgcheck sysfsutils
yum install -y --nogpgcheck kernel-devel
yum install -y --nogpgcheck rpm-build
yum install -y --nogpgcheck redhat-rpm-config
yum install -y --nogpgcheck readline-devel
yum install -y --nogpgcheck ncurses-devel