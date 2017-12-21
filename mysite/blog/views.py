# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BlogArticles

# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs":blogs})

def blog_article(request):#,article_id):
    #article = BlogArticles.objects.get(id=artice_id)
    #pub = article.publish
    return render(request, "blog/content.html")#, {"article":article,"publish":pub})
