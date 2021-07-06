from django.shortcuts import render, redirect
from CARRITO.models import Producto
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
from .models import Categoria
from .forms import formulario_contacto, formProducto, ProductoForm



from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    ultimos = Producto.objects.all().order_by('-id')[:3]
    otros = Producto.objects.all().order_by('-id')[3:10]
    return render(request,'home.html',{"ultimos":ultimos,"otros":otros})

def verProducto(request,id):
    # producto = get_object_or_404(Producto, id = id) 
    producto = Producto.objects.get(pk = id) 
    if producto:
        return render(request,'productos/verProducto.html',{'producto': producto})
    else:
        return render(request,'productos/verProducto.html',{'vacio': 'No existe'})
        
def buscar(request):
    if request.GET["inputProducto"]:
        # mensaje="Producto buscado: %r" %request.GET['inputProducto']
        producto = request.GET['inputProducto']
        if len(producto)>20:
            mensaje = "Texto de busqueda demasiado largo, intente otra vez"
        else:
            productos_encontrados_d = Producto.objects.filter(descripcion__icontains = producto)
            productos_encontrados_t = Producto.objects.filter(titulo__icontains = producto)
            
            productos_encontrados = productos_encontrados_d.union(productos_encontrados_t)
            return render(request,"productos/resultados_buqueda.html",{"productos_encontrados":productos_encontrados,"query":producto})
    else:
        return render(request,"productos/resultados_buqueda.html",{"productos_encontrados":'vacio'})
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

@login_required(login_url='login')
def carrito(request):
    if request.user.is_authenticated:
        return render(request,"carrito/carrito.html",{'carrito': 'carrito'})
    else:
        return render(request,"carrito/carrito.html", {'carrito': 'no hay carrito'})
 
@login_required(login_url='login')   
def agregarProducto(request):  
    if  request.method == "POST":
        form = ProductoForm(request.POST or None)
        img = ProductoForm(request.FILES)
        categoria = int(request.POST["categoria_id"])
        if form.is_valid():
            obj =  Producto()
            obj.titulo = form.cleaned_data['titulo']
            obj.descripcion = form.cleaned_data['descripcion']
            obj.imagenProducto = form.cleaned_data['imagenProducto']
            obj.precio = form.cleaned_data['precio']
            obj.categoria_id = categoria
            obj.save()
            
        else:
            return render(request,'productos/agregarProducto.html',{'error':'Error'})

             
    form = ProductoForm()
    return render(request,'productos/agregarProducto.html',{'form':form})
    
