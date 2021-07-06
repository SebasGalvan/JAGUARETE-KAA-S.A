from django.urls.conf import include
from USUARIOS import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login, name='Login'),
    path('registro/', views.registro, name='Registro'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    
]