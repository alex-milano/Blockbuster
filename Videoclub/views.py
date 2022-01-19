from operator import index
from pickle import GET
from django.shortcuts import render, redirect
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

def eliminar_pelicula(request,id):
    pelicula = Pelicula.objects.get(id = id)
    pelicula.delete()
    
    return render(request, 'confirmacionEliminado.html', {"pelicula": pelicula})

def formulario_modificacion(request,id):
    pelicula = Pelicula.objects.get(id = id)
    return render(request, 'formularioModificacion.html', {"pelicula": pelicula})

def modificar_pelicula(request):
    pelicula = Pelicula.objects.get(id = request.POST.get('Id'))

    nombre = request.POST.get('Nombre')
    categoria = request.POST.get('Categoria')
    descripcion = request.POST.get('Descripcion')
    precio = request.POST.get('Precio')

    pelicula.nombre = nombre
    pelicula.categoria = categoria
    pelicula.descripcion = descripcion
    pelicula.precio = precio
    pelicula.save()

    peliculas = Pelicula.objects.all()
    return render(request, 'listadoPeliculas.html',{"peliculas":peliculas})



