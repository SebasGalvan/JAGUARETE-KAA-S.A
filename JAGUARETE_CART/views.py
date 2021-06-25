from JAGUARETE_CART.models import Producto
from django.shortcuts import render

# Create your views here.


def productos(request):
    lista_productos =  Producto.objects.all()
    return render(request, 'productos/producto.html',{'lista_productos': lista_productos})