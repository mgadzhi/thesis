# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from users.admin import views


urlpatterns = patterns(
    '',
    url(r'^$', views.admins_list, name='admins_list'),
    url(r'^(?P<pk>\d+)/edit/$', views.admin_edit, name='admin_edit'),
    url(r'^(?P<pk>\d+)/$', views.admin_details, name='admin_details'),
)