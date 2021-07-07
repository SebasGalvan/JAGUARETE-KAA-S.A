from .models import Categoria

def extras(request):
    categorias =  Categoria.objects.all()
    return {'categorias':categorias}