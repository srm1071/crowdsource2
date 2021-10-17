from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login, name='login'),
    path('register', views.regi, name='register'),
    path('mapview', views.mapview, name='mapview'),
]

