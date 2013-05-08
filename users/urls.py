# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from users import views


urlpatterns = patterns('',
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/api/$', views.UserDetail.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserView.as_view()),
)