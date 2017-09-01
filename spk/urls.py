from django.conf.urls import url
from django.contrib import admin

from . import views as spk_url


urlpatterns = [    
    url(r'^$', spk_url.home, name='home'),
    url(r'^mail/$', spk_url.mailme, name='mail'),
    url(r'^blog/$', spk_url.myblog, name='blog'),
    url(r'^blog/(?P<id>\d+)/$', spk_url.blog_detail, name='detail'), 
    
]