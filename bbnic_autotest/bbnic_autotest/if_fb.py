# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import main

# receive POST request data
def if_top(request):
    ctx ={}
    if request.POST:
       # ctx['rlt'] = request.POST['q']
        ctx['rlt'] = main.welcome_message()
    return render(request, "if_fb.html", ctx)
