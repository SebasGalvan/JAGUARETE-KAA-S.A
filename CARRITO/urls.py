from CARRITO import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.inicio),
    path('buscar_producto/', views.buscar_producto),
    path('buscar/', views.buscar),
    path('contacto/', views.contacto, name='Contacto'),
    path('acerca_de/', views.acerca_de, name='Aacerca de'),
    path('producto/', views.producto, name='Producto'),
    path('carrito/', views.carrito, name='Carrito'),
]