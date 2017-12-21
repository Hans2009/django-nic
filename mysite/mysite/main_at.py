# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf

import sys,os
#sys.path.insert(0,'./tool/')
sys.path.append('/home/ubuntu17/Documents/shared/github/dj/mysite/mysite/tool/')
import ssh_cmd
import scp_sendrecv
sys.path.append('/home/ubuntu17/Documents/shared/github/dj/mysite/mysite/vendor/opa/')
import opa_testcase



#sys.path.insert(0,'./testcase/')
#sys.path.insert(0,'./testcase/tc0/')
#globle variables
ip = '10.245.36.66'
port = '22'
usr  = 'root'
passwd = '111111'
#cmd = 'ifconfig'
cmd = 'uname -a'

# receive POST request data
#def if_top(request):
def main_my(request):
    ctx  ={}
    if request.POST:
        ctx['rlt'] = ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'ifconfig')

        ctx['rlt1'] = request.POST['Vender']
        ctx['rlt2'] = request.POST['OS']
        ctx['rlt3'] = request.POST['testcase']
        ctx['rlt4'] = request.POST['oss_number']

        oss_number  = request.POST['oss_number']
        ctx['rlt']  = opa_testcase.opa_tc0(ip,port,usr,passwd,oss_number)



    return render(request, "home.html", ctx)







#############################
