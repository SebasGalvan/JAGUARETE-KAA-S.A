from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    descripcion = models.TextField(max_length=100)
    
    
class Producto(models.Model):
    titulo =  models.CharField(max_length=100)
    imagenProducto =  models.ImageField(upload_to='productos',blank = True, null = True)
    descripcion = models.CharField(max_length=100)
    precio =  models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete= models.CASCADE, null=False)

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    listaProductos = models.ManyToManyField(Producto)
    total = models.FloatField() 
    
    