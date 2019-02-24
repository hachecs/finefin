# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #-- Banks
    # url(r'^banks/$', views.banks, name='banks'),
    #-- Banks add
    url(r'^banks/begin/add/$', views.banks_begin_add, name='banks_begin_add'),
]
