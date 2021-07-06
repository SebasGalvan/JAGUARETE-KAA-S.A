from django.shortcuts import render
from .forms import formularioLogin, formularioRegistro


# Create your views here.


def registro(request):
    form = formularioRegistro
    return render(request,'registration/registro.html',{'form':form})

def login(request):
    form = formularioLogin
    return render(request,'registration/login.html',{'form':form})


# def salir(request):
#     return render(request,'registration/logged_out.html')
    