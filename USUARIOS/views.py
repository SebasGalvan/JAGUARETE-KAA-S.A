from django.shortcuts import render
from .forms import formularioLogin, formularioRegistro
from django.contrib.auth.models import User


# Create your views here.


def registro(request):
    
    if request.POST:
        
        
        user =  request.POST['username']
        password =  request.POST['password']
        nombre =  request.POST['nombre']
        apellido =  request.POST['apellido']
        email =  request.POST['email']
        
        usuario  = User.objects.create_user(user, email, password)
        usuario.first_name = nombre
        usuario.last_name = apellido

        usuario.save()
        
        form = formularioLogin
        return render(request,'registration/login.html',{'form':form})
        
    else:
        form = formularioRegistro
        return render(request,'registration/registro.html',{'form':form})




def login(request):
    form = formularioLogin
    return render(request,'registration/login.html',{'form':form})


# def salir(request):
#     return render(request,'registration/logged_out.html')
    