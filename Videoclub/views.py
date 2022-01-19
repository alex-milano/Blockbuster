from http.client import HTTPResponse
from operator import index
from pickle import GET
from django.template import loader
from django.shortcuts import render, redirect
from Videoclub.forms import Formulario_peliculas
from Videoclub.models import Pelicula


def index(request):
    return render(request, 'index.html')


def formulario_peliculas(request):
    return render(request, 'formularioPeliculas.html')


def listado_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'listadoPeliculas.html', {"peliculas": peliculas})


def alta_pelicula(request):

    pelicula = Pelicula(nombre=request.POST.get('Nombre'),
    categoria = request.POST.get('Categoria'),
    descripcion = request.POST.get('Descripcion'),
    precio = request.POST.get('Precio') )
    
    pelicula.save()
    
    return render(request, 'confirmacionAlta.html', {'pelicula': pelicula})



