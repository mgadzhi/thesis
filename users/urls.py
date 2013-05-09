# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'agents', views.AgentViewSet)
router.register(r'resellers', views.ResellerViewSet)
router.register(r'admins', views.AdminViewSet)

print router.urls

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>\d+)/api/$', views.UserDetail.as_view()),
    # url(r'^users/(?P<pk>\d+)/$', views.UserView.as_view()),
)