# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import main
import sys
sys.path.insert(0,'./tool/')
sys.path.insert(0,'./testcase/')
import ssh_cmd

# receive POST request data
def if_top(request):
    ctx ={}
    if request.POST:
        #ctx['rlt'] = request.POST['q']
        #ctx['rlt'] = main.welcome_message()
        ctx['rlt'] = ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','ifconfig') 
        return render(request, "if_fb.html", ctx)
