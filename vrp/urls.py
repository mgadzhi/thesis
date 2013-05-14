# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from vrp import views


urlpatterns = patterns(
    '',
    url(r'^/$', views.index),
    url(r'^orders/$', views.orders_list),
    url(r'^orders/create/$', views.order_create),
    url(r'^stations/$', views.stations_list),
    url(r'^stations/create/$', views.station_create, name="create_station"),
)