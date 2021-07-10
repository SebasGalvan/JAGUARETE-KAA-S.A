from django.shortcuts import render
from .forms import formularioLogin, formularioRegistro
from django.contrib.auth.models import User
from CARRITO.models import Producto


# Create your views here.


def registro(request):
    
    if request.POST:
        
        user =  request.POST['usuario']
        password =  request.POST['password']
        nombre =  request.POST['nombre']
        apellido =  request.POST['apellido']
        email =  request.POST['email']
        
        usuario  = User.objects.create_user(user, email, password)
        usuario.first_name = nombre
        usuario.last_name = apellido
        
        super = request.POST['super']
        if super:
            usuario.is_staff = True
            usuario.save()
            ultimos = Producto.objects.all().order_by('-id')[:3]
            for pr in ultimos:
                pr.titulo =  pr.titulo[:43]
                otros = Producto.objects.all().order_by('-id')[3:10]
            return render(request,'home.html',{"ultimos":ultimos,"otros":otros})
        
        usuario.save()
        form = formularioLogin
        return render(request,'registration/login.html',{'form':form})
        
    
    form = formularioRegistro
    return render(request,'registration/registro.html',{'form':form})




def login(request):
    form = formularioLogin
    return render(request,'registration/login.html',{'form':form})


# def salir(request):
#     return render(request,'registration/logged_out.html')
    