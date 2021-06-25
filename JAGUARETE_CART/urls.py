from django.urls import path
from . import views

app_name = "JAGUARETE_CART"

urlpatterns = [
    path('/productos',views.productos,name='productos')
]
