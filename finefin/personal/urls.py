# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #-- Personal
    url(r'^add/$', views.personal_add, name='personal_add'),
]
