# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from vrp import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index),
    url(r'^orders/$', views.orders_list, name="orders_list"),
    url(r'^orders/create/$', views.order_create, name="create_order"),
    url(r'^orders/active-orders/$', views.active_orders, name="active_orders"),
    url(r'^stations/$', views.stations_list, name="stations_list"),
    url(r'^stations/create/$', views.station_create, name="create_station"),
    url(r'^vehicles/$', views.vehicles_list, name="vehicles_list"),
    url(r'^vehicles/create/$', views.vehicle_create, name="create_vehicle"),
    url(r'^executed-orders/$', views.tasks_list, name="tasks_list"),
    url(r'^do-execute-active-orders/$', views.do_execute_active_orders, name="execute_orders"),
)