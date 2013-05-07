# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from vrp.reseller import views


urlpatterns = patterns(
    '',
    url(r'(?P<id>\d+)/$', views.reseller_info),
)