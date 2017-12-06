from django.shortcuts import render
#import sys
#sys.path.insert(0,'/hans/work/bbnic_autotest/bbnic_autotest/')
import main

def hello(request):
   #return HttpResponse("Hello world!")
    context = {}
    #context['hello'] = 'Hello World! This is from template'
    context['hello'] = main. welcome_message() 
    print("hello world! This is view.py") 
    return render(request, 'hello.html',context)
