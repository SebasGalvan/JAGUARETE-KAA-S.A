from django import forms

class formulario_contacto(forms.Form):
    asunto=  forms.CharField()
    email = forms.EmailField()
    mensaje =  forms.CharField()