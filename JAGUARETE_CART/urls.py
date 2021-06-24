from django.urls import path
from . import views

app_name = "JAGUARETE_CART"

urlpatterns = [
    path('',views.index,name='index'),
    path('/productos',views.productos,name='productos')
]
