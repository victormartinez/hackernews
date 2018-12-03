from django.contrib import admin
from django.urls import include, path

from hackernews.accounts import views


app_name = 'accounts'

urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login'),
]
