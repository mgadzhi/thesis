# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from users import views
from .admin import urls as admin_urls
from .reseller import urls as reseller_urls
from .agent import urls as agent_urls

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'agents', views.AgentViewSet)
router.register(r'resellers', views.ResellerViewSet)
router.register(r'admins', views.AdminViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin_urls)),
    url(r'^reseller/', include(reseller_urls)),
    url(r'^agent/', include(agent_urls)),
    # url(r'^admins/$', views.admins_list, name='admins_list'),
    # url(r'^admins/(?P<pk>\d+)/edit/$', views.admin_edit, name='admin_edit'),
    # url(r'^admins/(?P<pk>\d+)/$', views.admin_details, name='admin_details'),
)