
from django import forms
from django.forms import fields
from .models import Carrito, Producto, Categoria

class formulario_contacto(forms.Form):
    asunto=  forms.CharField()
    email = forms.EmailField()
    mensaje =  forms.CharField()
class ProductoForm(forms.ModelForm):
    categoria_id =forms.ModelChoiceField(queryset=Categoria.objects.all())
    class Meta:
        
        model = Producto
        fields = ['titulo', 'imagenProducto', 'descripcion','precio',]
   
class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['usuario', 'productos' , 'cantidad']

        
