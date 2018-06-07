# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py
   Description :
   Author :       Lychlov
   date：          2018/6/6
-------------------------------------------------
   Change Activity:
                   2018/6/6:
-------------------------------------------------
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
