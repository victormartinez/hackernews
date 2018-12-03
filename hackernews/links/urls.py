from django.contrib import admin
from django.urls import include, path

from . import views


app_name = 'links'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
]
