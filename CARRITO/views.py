from django.shortcuts import render
from CARRITO.models import Producto
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from CARRITO.forms import formulario_contacto

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def buscar_producto(request):
    return render(request,"formularios/formBusquedaProductos.html")

def buscar(request):
    
    if request.GET["inputProducto"]:
        # mensaje="Producto buscado: %r" %request.GET['inputProducto']
        producto = request.GET['inputProducto']
        if len(producto)>20:
            mensaje = "Texto de busqueda demasiado largo, intente otra vez"
        else:
            productos_encontrados = Producto.objects.filter(descripcion__icontains = producto)
            return render(request,"productos/resultados_buqueda.html",{"productos_encontrados":productos_encontrados,"query":producto})
    else:
        mensaje = "Campo de busqueda Vacio"
    return HttpResponse(mensaje)


def contacto(request):
    
    if request.method=="POST":
        
        mi_formulario = formulario_contacto(request.POST)
        
        if mi_formulario.is_valid():
            
            informacion_formulario =  mi_formulario.cleaned_data
            
            send_mail(informacion_formulario['asunto'],informacion_formulario['mensaje'],informacion_formulario.get('email',''),['sebastiangalvan.ar@gmail.com'],)
            
            return render(request,"contacto/gracias.html")
    else:
        mi_formulario =  formulario_contacto()
            
    return render(request,"contacto/contacto.html",{"formulario":mi_formulario})


def acerca_de(request):
    return render(request,"acerca_de.html")

def producto(request):
    return render(request,"productos/producto.html")

def carrito(request):
    return render(request,"carrito/carrito.html")
