# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf

import sys,os
sys.path.insert(0,'./tool/')
import ssh_cmd
import scp_sendrecv

#sys.path.insert(0,'./testcase/')
sys.path.insert(0,'./testcase/tc0/')

#globle variables
ip = '192.168.223.130'
port = '22'
usr  = 'root'
passwd = '1111111'
#cmd = 'ifconfig'
cmd = 'uname -a'

# receive POST request data
def if_top(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        #ctx['rlt'] = main.welcome_message()
        ctx['rlt'] = ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'ifconfig') 

        ctx['rlt'] = opa_tc0()
    return render(request, "if_fb.html", ctx)



##############################################################
def opa_tc0():
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir /opa/')
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir /opa/tc0/')
    
    testcase_path = '/opa/tc0/'
    for file_name in os.listdir(testcase_path):
        file_path = os.path.join(testcase_path,file_name)
        print(file_path)
        #scp_sendrecv.ssh_scp_put(ip,port,usr,passwd,file_path,file_path)


    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir -p /opa/oss/88905')
    oss_path = '/opa/oss/88905/'
    for file_name in os.listdir(oss_path):
        file_path = os.path.join(oss_path,file_name)
        print(file_path)
        #scp_sendrecv.ssh_scp_put(ip,port,usr,passwd,file_path,file_path)

    #ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'tar zxvf /opa/oss/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134.tgz -C /opa/oss/88905/')
    #ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'source /opa/oss/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134/./INSTALL -a')
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'source /opa/tc0/driver.sh')
    
    return 'opa_tc0 successfully'







