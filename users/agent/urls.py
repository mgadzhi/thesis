# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from users.agent import views


urlpatterns = patterns(
    '',
    url(r'edit/$', views.agent_edit, name='agent_edit'),
    url(r'^$', views.agent_details, name='agent_details'),
)