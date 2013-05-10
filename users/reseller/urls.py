# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from users.reseller import views


urlpatterns = patterns(
    '',
    url(r'^$', views.resellers_list, name='resellers_list'),
    url(r'^(?P<reseller_pk>\d+)/edit/$', views.reseller_edit, name='reseller_edit'),
    url(r'^(?P<reseller_pk>\d+)/$', views.reseller_details, name='reseller_details'),
)