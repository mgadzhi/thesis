from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from vrp import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thesis.views.home', name='home'),
    # url(r'^thesis/', include('thesis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^signin/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^signout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^api/', include('users.urls'))
)
