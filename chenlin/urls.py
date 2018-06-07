# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py
   Description :
   Author :       Lychlov
   date：          2018/6/7
-------------------------------------------------
   Change Activity:
                   2018/6/7:
-------------------------------------------------
"""
from django.urls import path

from chenlin import views

urlpatterns = [
    path('', views.index, name='index'),

]