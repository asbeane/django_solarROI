"""solarROI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from solarROI.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'solarROI.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^confirm/([A-Za-z0-9]*)$', ('solarROI.views.register_success')),
    url(r'^confirm/(?P<activation_key>\w+)/', ('solarROI.views.register_success')),
    url(r'^logout/$', 'solarROI.views.logout'),
    url(r'^login/$', 'solarROI.views.login'),
    url(r'^auth/$', 'solarROI.views.auth_view'),
    url(r'^logout/$', 'solarROI.views.logout'),
    url(r'^loggedin/$', 'solarROI.views.loggedin'),
    url(r'^invalid/$', 'solarROI.views.invalid_login'),
    url(r'^register/$', 'solarROI.views.register_user'),
    url(r'^register_success/$', 'solarROI.views.register_success'),
    url(r'^register/register_success/', 'solarROI.views.register_success'),
    url(r'^solarROI/$', 'solarROI.views.solarROI'),
)
