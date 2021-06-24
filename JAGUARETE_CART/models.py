from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion =  models.CharField(max_length=64)

    def  __str__(self):
        return f' Categoria #{self.id}: {self.descripcion}'


class Producto(models.Model):
    titulo =  models.CharField(max_length=64)
    descripcion =  models.CharField(max_length=64)
    imagen = models.ImageField(upload_to = 'productos', null=True)
    precio = models.FloatField()
    stock =  models.IntegerField()
    categoria =  models.ForeignKey(Categoria, on_delete=models.CASCADE , related_name='categoria_producto')
    
    def __str__(self):
        return f'ID :# {self.id} , {self.titulo} {self.descripcion} {self.imagen} {self.categoria}'

class Carrito(models.Model):
    # usuario =  models.ForeignKey();
    lista_productos =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    total =  models.FloatField()
    
    