from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^company/(?P<pk>[0-9]+)/remove/$', views.company_remove, name='company_remove'),
    url(r'^company/(?P<pk>[0-9]+)/edit/$', views.company_edit, name='company_edit'),
]
