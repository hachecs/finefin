# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #-- Dashboard
    url(r'^$', views.dashboard, name='dashboard'),
    #-- Login
    url(r'^login/$', views.authorization, name='login'),
    #-- Logout
    url(r'^logout/$', views.authorization_logout, name='logout'),
]
