from django.shortcuts import render
from .forms import *
# Create your views here.


def registro(request):
    # usuario = request.GET['inputProducto']
    # email = request.GET['inputProducto']
    # password = request.GET['inputProducto']
    # first_name = request.GET['inputProducto']
    # last_name = request.GET['inputProducto']

    # user = User.objects.create_user(usuario, email, password)

    # # Update fields and then save again
    # user.first_name = 'John'
    # user.last_name = 'Citizen'
    # user.save()
    return render(request,'registration/registro.html')


def login(request):
    return render(request,'registration/login.html')

def salir(request):
    return render(request,'registration/logged_out.html')
    