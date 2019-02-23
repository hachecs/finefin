# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #-- Signup
    url(r'^$', views.signup, name='signup'),
    #-- Signup done
    url(r'^done/$', views.signup_done, name='signup_done'),
]
