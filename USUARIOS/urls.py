from abc import abstractproperty
from django.urls import path, include
from . import views

app_name = "USUARIOS"
urlpatterns = [
    path('',views.login, name='login'),
    path('registrarse/',views.registrarse, name='registrarse')
]
