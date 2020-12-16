from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.Client_list, name='Client_list'),
path('rentcontract/', views.RentContract_list, name='RentContract_list'),
path('premises/', views.Premises_list, name='Premises_list'),
path(r'new/', views.Client_edit, name='Client_edit')
]