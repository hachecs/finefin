# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #-- Signup
    url(r'^$', views.signup, name='signup'),
    #-- Signup done
    url(r'^done/$', views.signup_done, name='signup_done'),
    #-- Signup activation
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.signup_activate, name='signup_activate'),
]
