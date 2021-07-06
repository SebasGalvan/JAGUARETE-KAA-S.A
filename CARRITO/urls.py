from django.urls.conf import include
from CARRITO import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



# app_name = "CARRITO"
urlpatterns = [
    path('', views.inicio, name='Home'),
    path('buscar/', views.buscar, name='Buscar'),
    path('contacto/', views.contacto, name='Contacto'),
    path('acerca_de/', views.acerca_de, name='Aacerca de'),
    path('producto/', views.producto, name='Producto'),
    path('carrito/', views.carrito, name='Carrito'),
    path('producto/<int:id>/', views.verProducto, name='verProducto'), 
    path('USUARIO/', include('USUARIOS.urls')), 
    path('agregarProducto/', views.agregarProducto, name='Agregar'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)