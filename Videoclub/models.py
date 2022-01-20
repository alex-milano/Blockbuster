from ast import Str
import email
from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length= 100)
    categoria = models.CharField(max_length= 100)
    descripcion = models.CharField(max_length=100)
    #estado = models.BooleanField()
    precio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'


class Socio(models.Model):
    nombre = models.CharField(max_length= 50)
    nro_socio = models.CharField(max_length= 6)
    telefono = models.CharField(max_length= 10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre}'


class Empleado(models.Model):
    nombre= models.CharField(max_length= 100)
    dni = models.CharField(max_length= 100)
    telefono = models.CharField(max_length= 100)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre}'
    
