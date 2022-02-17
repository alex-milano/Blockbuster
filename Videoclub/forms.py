from urllib import request
from django import forms

class Formulario_peliculas(forms.Form):
    nombre = forms.CharField(max_length= 100)
    categoria = forms.CharField(max_length= 100)
    descripcion = forms.CharField(max_length=100)
    estado = forms.BooleanField()
    precio = forms.IntegerField()
