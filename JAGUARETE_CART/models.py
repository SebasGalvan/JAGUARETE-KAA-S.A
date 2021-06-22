from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion =  models.CharField(max_length=255)
