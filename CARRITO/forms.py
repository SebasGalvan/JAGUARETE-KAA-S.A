
from django import forms
from .models import Producto, Categoria

class formulario_contacto(forms.Form):
    asunto=  forms.CharField()
    email = forms.EmailField()
    mensaje =  forms.CharField()
    
class formProducto(forms.Form):
    
    titulo =  forms.CharField(max_length=100)
    imagenProducto = forms.ImageField()
    descripcion = forms.CharField(max_length=200)
    precio = forms.FloatField()
    categoria_id = forms.ModelChoiceField(queryset=Categoria.objects.all())
    class Meta:
        model = Producto
        fields = ['titulo', 'imagenProducto', 'descripcion' , 'precio', 'categoria_id']

class ProductoForm(forms.ModelForm):
    categoria_id =forms.ModelChoiceField(queryset=Categoria.objects.all())
    class Meta:
        
        model = Producto
        fields = ['titulo', 'imagenProducto', 'descripcion','precio',]
 

   
           
        
