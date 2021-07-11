from django.shortcuts import render
from CARRITO.models import Producto
from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
from .models import Categoria
from .forms import formulario_contacto, ProductoForm, CarritoForm
from django.db.models import Q



from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    ultimos = Producto.objects.all().order_by('-id')[:3]
    for pr in ultimos:
        pr.titulo =  pr.titulo[:43]
        pr.descripcion =  pr.descripcion[:70]
    otros = Producto.objects.all().order_by('-id')[3:10]
    return render(request,'home.html',{"ultimos":ultimos,"otros":otros})

def verProducto(request,id):
    producto = Producto.objects.get(pk = id) 
    if producto:
        return render(request,'productos/verProducto.html',{'producto': producto})
    else:
        return render(request,'productos/verProducto.html',{'vacio': 'No existe'})
        
def buscar(request):
    producto = request.GET['inputProducto']
    if request.GET:
        if len(producto)>20:
            mensaje = "Texto de busqueda demasiado largo, intente otra vez"
            return render(request,"",{"mensaje":mensaje,'query':producto})
        else:
            productos_encontrados_d = Producto.objects.filter(descripcion__icontains = producto)
            productos_encontrados_t = Producto.objects.filter(titulo__icontains = producto)
            
            productos_encontrados = productos_encontrados_d.union(productos_encontrados_t)
            return render(request,"productos/resultados_buqueda.html",{"productos_encontrados":productos_encontrados,"query":producto})
    else:
        return render(request,"productos/resultados_buqueda.html",{"mensaje":'No se encontraron Productos','query':producto})



def contacto(request):
    if request.method=="POST":
        mi_formulario = formulario_contacto(request.POST)
        if mi_formulario.is_valid():
            informacion_formulario =  mi_formulario.cleaned_data
            send_mail(informacion_formulario['asunto'],informacion_formulario['mensaje'],informacion_formulario.get('email',''),['miemail@gmail.com'],)
            return render(request,"contacto/gracias.html")
    mi_formulario =  formulario_contacto()
    return render(request,"contacto/contacto.html",{"formulario":mi_formulario})


def acerca_de(request):
    return render(request,"acerca_de.html")

def producto(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.titulo =  producto.titulo[:43]
        producto.descripcion =  producto.descripcion[:60]
    return render(request,"productos/producto.html",{'productos':productos})



@login_required(login_url='login')
def productoEditar(request, id):
    
    if request.method=="POST": 

        prod = Producto.objects.get(pk=id)
        
        categoria = int(request.POST['categoria_id'])
        
        titulo = request.POST['titulo']
        if titulo:
            prod.titulo = titulo   
            
        descripcion  = request.POST['descripcion']
        if descripcion:
            prod.descripcion = descripcion
        
        precio = request.POST['precio']
        if precio:
            prod.precio = (precio)
        
        if request.FILES.get('imagenProducto'):
            prod.imagenProducto.delete()
            prod.imagenProducto = request.FILES.get('imagenProducto')
        
        if categoria:  
            prod.categoria_id = categoria
        
        prod.save()
        return render(request,'productos/verProducto.html',{'producto': prod})
              
    producto = Producto.objects.get(pk = id)
    categorias = Categoria.objects.all()
    form = ProductoForm(request.POST)
    return render (request,'productos/editar.html',{'form':form, 'producto':producto, 'categorias':categorias})

def productoEliminar(request, id):
    Producto.objects.filter(pk=id).delete()
    mensaje = "Producto eliminado."
    productos =  Producto.objects.all()
    for producto in productos:
        producto.titulo =  producto.titulo[:43]
        producto.descripcion =  producto.descripcion[:60]
    return render (request, 'productos/producto.html',{'productos':productos, 'mensaje':mensaje})
   
    





@login_required(login_url='login')
def carrito(request):
    
    user = request.user
    id_user =  user.id
    productos =  Carrito.objects.filter(usuario_id = id_user).select_related('productos')
    
    total = 0
    for p in productos:
        producto = Producto.objects.get(pk = p.productos_id)
        total = total + (producto.precio* p.cantidad)        
    if request.user.is_authenticated:
        return render(request,"carrito/carrito.html",{'carrito': productos, 'vacio':'No tiene productos en su carrito', 'total':total})
    else:
        return render(request,"carrito/carrito.html", {'vacio': 'No tiene productos en su carrito'})   
    
@login_required(login_url='login')   
def agregarCarrito(request ,id):
    user = request.user
    producto =  Producto.objects.get(pk = id)
    existente = Carrito.objects.filter(Q(usuario_id=user.id) & Q(productos_id=id)).exists()
    
    if existente:
        art = Carrito.objects.get(Q(usuario_id=user) & Q(productos_id=producto))
        cant = art.cantidad + 1 
        Carrito.objects.filter(Q(usuario_id=user.id) & Q(productos_id=id)).update(cantidad = cant)
        return render(request,'productos/verProducto.html',{'producto': producto,'mensaje':'Modifico la cantidad en un producto de su carrito'})
    else:
        cantidad = 1
        form =  CarritoForm({'usuario':user , 'producto':producto, 'cantidada':cantidad})
        if form.is_valid:
            obj = Carrito()
            obj.usuario = user
            obj.productos = producto
            obj.cantidad = cantidad
            obj.save()
            return render(request,'productos/verProducto.html',{'producto': producto, 'mensaje' : 'Producto agregado al carrito'})

def eliminarDelCarrito(request,id):
    user = request.user

    Carrito.objects.filter(Q(usuario_id=user.id) & Q(productos_id = id)).delete()
    
    productos =  Carrito.objects.filter(usuario_id = user.id)
    return render(request,"carrito/carrito.html", {'carrito': productos,'mensaje': 'No tiene productos en su carrito','vacio':'Su carrito esta vacio'}) 
   
    
    
 
@login_required(login_url='login')   
def agregarProducto(request):  
    if  request.method == "POST":
        form = ProductoForm(request.POST or None)
        categoria = int(request.POST["categoria_id"])
        # imagen = str(request.POST["imagenProducto"])
        if form.is_valid():
            obj =  Producto()
            obj.titulo = form.cleaned_data['titulo']
            obj.descripcion = form.cleaned_data['descripcion']
            obj.imagenProducto = request.FILES.get('imagenProducto')
            obj.precio = form.cleaned_data['precio']
            obj.categoria_id = categoria
            obj.save()
            mensaje = f'Producto: {obj.titulo} agregado.' 
            form = ProductoForm()
            return render(request,'productos/agregarProducto.html',{'form':form, 'mensaje':mensaje})
            
        else:
            return render(request,'productos/agregarProducto.html',{'error':'Error'})

             
    form = ProductoForm()
    categorias =  Categoria.objects.all()
    return render(request,'productos/agregarProducto.html',{'form':form,'categorias':categorias})

def agregarCategoria(request):
    
    if request.method == "POST":
        descripcion = request.POST["descripcion"]
        obj =  Categoria()
        obj.descripcion = descripcion
        obj.save()
        form = ProductoForm()
        return render(request,'productos/agregarProducto.html',{'form': form})   
    else:
        return render(request,'productos/agregarCategoria.html')
    
def productoCategoria(request, id):
    categoria =  Categoria.objects.get(pk = id)
    if  request.method == "GET": 
        productos = Producto.objects.filter(categoria_id = id)
        if productos:
            return render(request,'productos/resultados_buqueda.html',{'productos': productos,'categoria':categoria.descripcion})
        else:
            return render(request,'productos/resultados_buqueda.html',{'mensaje': 'No hay productos con esta categoria','categoria':categoria.descripcion})
        
        
        
def vaciarCarrito(request):
    user = request.user
    id_user = user.id
    Carrito.objects.filter(usuario_id = id_user).delete()
    
    productos =  Carrito.objects.filter(usuario_id = user.id)
    return render(request,"carrito/carrito.html", {'carrito': productos,'mensaje': 'No tiene productos en su carrito','vacio':'Su carrito esta vacio'}) 