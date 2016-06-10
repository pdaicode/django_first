# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
#from . import views

urlpatterns = patterns('developing.views',
    url(r'^/$', 'list', name='list'),
)

#urlpatterns = [
#	url(r'^$', 'views.list', name='list'),
#]
#url(r'^list/$', 'list', name='list'),