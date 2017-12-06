# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf

import sys
sys.path.insert(0,'./tool/')
import ssh_cmd

#sys.path.insert(0,'./testcase/')
sys.path.insert(0,'./testcase/tc0/')

# receive POST request data
def if_top(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        #ctx['rlt'] = main.welcome_message()
        #ctx['rlt'] = ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','ifconfig') 
        #ctx['rlt'] = ssh_cmd.ssh_scp_put('192.168.182.129','22','root','1111111','ifconfig') 
        ctx['rlt'] = ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','pwd') 
        ctx['rlt'] = ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','cd /root/opa/') 
        ctx['rlt'] = ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','pwd') 
        ctx['rlt'] = ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','source ./opa/tc0.sh') 
        #ctx['rlt'] = ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','./tc0.sh') 
        return render(request, "if_fb.html", ctx)
