# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BlogArticles
from django.http import HttpResponse
from django.http import StreamingHttpResponse

# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs":blogs})

def blog_article(request):#,article_id):
    #article = BlogArticles.objects.get(id=artice_id)
    #pub = article.publish
    return render(request, "blog/content.html")#, {"article":article,"publish":pub})

##################################################################
def download_file(request):
    # do something
    the_file_name='log'
    filename='./log/log'
    response=StreamingHttpResponse(readFile(filename))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="{0}"'.format(the_file_name)
    return response

def readFile(filename,chunk_size=512):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break
