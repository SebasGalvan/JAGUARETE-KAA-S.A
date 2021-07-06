from django import forms
from django.contrib.auth.admin import User

class formularioLogin(forms.Form):
    
    username =  forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User


class formularioRegistro(forms.Form):
    
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    verificacion_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    nombre= forms.CharField()
    apellido = forms.CharField()

    class Meta:
        model = User