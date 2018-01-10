# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf

import sys,os,time
#sys.path.insert(0,'./tool/')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/tool')
import ssh_cmd
import scp_sendrecv
import ping_timeout
#sys.path.insert(0,'./opa/')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/opa')
import opa_testcase
import opa_entry

#globle variables
#ip = '192.168.81.129'
port   = '22'
usr    = 'root'
passwd = '111111'
cmd    = 'uname -a'

# receive POST request data
def main_my(request):
    ctx  ={}

    print("--------------------directory----------------")
    print("os.path.dirname__file__:%s" %os.path.dirname(os.path.abspath(__file__)))
    print("os.path.dirname__file__:%s" %os.path.dirname(os.path.abspath('./')))
    print("--------------------directory----------------")

    if request.POST:

        ip          = request.POST['web_ip']
        vendor      = request.POST['web_vendor']
        os_type     = request.POST['web_os_type'] # RHEL73 RHEL74
        oss_number  = request.POST['web_oss_number']
        tc_number   = request.POST['web_testcase']

        ctx['rlt1'] = vendor
        ctx['rlt2'] = os_type
        ctx['rlt3'] = oss_number
        ctx['rlt4'] = tc_number

        print "Start : %s" % time.ctime()

        if vendor == 'OmniPath':
            ctx['rlt5'] = opa_entry.opa_entry_cli(ip,port,usr,passwd,oss_number,tc_number)
        elif vendor == 'Qlogic':
            print("Qlogic not supported now!")
        else:
            print("Please choose your own vendor")


    return render(request, "home.html", ctx)



#############################
