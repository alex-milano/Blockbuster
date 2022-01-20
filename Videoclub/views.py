import email
from operator import index
from pickle import GET
from django.shortcuts import render, redirect
from Videoclub.models import Pelicula, Socio


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

def formulario_socio(request):
    return render(request, 'formularioSocio.html')


def confirmacion_alta_socio(request):
    socio = Socio(nombre= request.POST.get('Nombre'),
    nro_socio = request.POST.get('Numero'),
    telefono = request.POST.get('Telefono'),
    email = request.POST.get('Email'))
    socio.save() 
    return render(request, 'confirmacionAltaSocio.html', {'socio': socio})

def listado_socios(request):
    socios = Socio.objects.all()
    return render(request,'listadoSocios.html', {'socios': socios})

def eliminar_socio(request, id):
    socio = Socio.objects.get(id=id)
    socio.delete()
    socios = Socio.objects.all()
    return render(request,'listadoSocios.html', {'socios':socios})


def formulario_modificacion_socio(request, id):
    socio = Socio.objects.get(id = id)
    return render(request, 'formularioModificacionSocio.html', {'socio':socio})

def modificar_socio(request):
    id = request.POST.get('Id')
    nombre = request.POST.get('Nombre')
    nro_socio = request.POST.get('Numero')
    telefono = request.POST.get('Telefono')
    email = request.POST.get('Email')

    socio = Socio.objects.get(id = id)
    socio.nombre = nombre
    socio.nro_socio = nro_socio
    socio.telefono = telefono
    socio.email = email
    socio.save()
    socios = Socio.objects.all()

    return render(request, 'listadoSocios.html', {'socios':socios})
    





