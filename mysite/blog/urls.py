from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_title,name="blog_title"),
    url(r'^content$',views.blog_article,name="blog_article"),
    url(r'^download$',views.download_file, name='user_dl'),
]
