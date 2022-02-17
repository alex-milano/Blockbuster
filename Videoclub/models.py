from ast import Str
from distutils.command.upload import upload
from django.contrib.auth.models import User
import email
from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length= 100, default='DEFAULT VALUE')
    categoria = models.CharField(max_length= 100)
    descripcion = models.CharField(max_length=100)
    #estado = models.BooleanField()
    precio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} - categoria {self.categoria} - descripcion {self.descripcion} - precio {self.precio}'


class Socio(models.Model):
    nombre = models.CharField(max_length= 50, default='DEFAULT VALUE')
    nro_socio = models.CharField(max_length= 6)
    telefono = models.CharField(max_length= 10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} - nro_socio {self.nro_socio} - telefono {self.telefono} - email {self.email}'


class Empleado(models.Model):
    nombre = models.CharField(max_length= 100, default='DEFAULT VALUE')
    dni = models.CharField(max_length= 100)
    telefono = models.CharField(max_length= 100)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre}'

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null = True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"
