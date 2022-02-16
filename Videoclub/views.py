import email
from operator import index
from pickle import GET
from django.shortcuts import render, redirect
from Videoclub.models import Avatar
from Videoclub.models import Empleado, Pelicula, Socio

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def inicio(request):

    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, "index.html", {'url': avatar[0].imagen.url})


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
    

def listado_empleados(request):
    empleados = Empleado.objects.all()
    return render(request,'listadoEmpleados.html',{'empleados':empleados})

def formulario_empleado(request):
    return render(request,'formularioEmpleado.html')

def confirmacion_alta_empleado(request):
    empleado = Empleado(nombre = request.POST.get('Nombre'),
    dni = request.POST.get('Dni'),
    telefono = request.POST.get('Telefono'),
    email = request.POST.get('Email')
    )
    empleado.save()
    return render(request,'confirmacionAltaEmpleado.html', {'empleado':empleado})

def formulario_modificacion_empleado(request, id):
    empleado = Empleado.objects.get(id = id)
    return render(request, 'formularioModificacionEmpleado.html', {'empleado':empleado})

def modificar_empleado(request):
    id = request.POST.get('Id')
    nombre = request.POST.get('Nombre')
    dni = request.POST.get('Dni')
    telefono = request.POST.get('Telefono')
    email = request.POST.get('Email')

    empleado = Empleado.objects.get(id = id)
    empleado.nombre = nombre
    empleado.dni = dni
    empleado.telefono = telefono
    empleado.email = email
    empleado.save()
    empleados = Empleado.objects.all()

    return render(request, 'listadoEmpleados.html', {'empleados':empleados})

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    empleados = Empleado.objects.all()
    return render(request,'listadoEmpleados.html', {'empleados':empleados})


def login_request(request):

    if (request.method == 'POST'):

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            data = form.cleaned_data

            user = authenticate(username=data['username'], password=data['password'])

            if user is not None: 
            
                login(request, user)
                return render(request,'index.html', {"mensaje": f"Bienvenido {user.get_username()}"})
                
            else:
                return render(request,'index.html', {"mensaje": f"Falló la autenticación"})
        else: 
                return render(request,'index.html', {"mensaje": f"Error, formulario erroneo"}) 
           
    form = AuthenticationForm()

    return render(request,"login.html",{'form':form})

def register(request):

    if(request.method == 'POST'): 

        form = UserCreationForm(request.POST)

        if(form.is_valid()):

            username = form.cleaned_data['username']
            form.save()

            return render(request,"index.html", {'mensaje': 'Usuario creado con exito'})
        
        else: 

            return render(request,"index.html", {'mensaje': 'Usurio no creado, intente nuevamente'})

    else: 

        form = UserCreationForm()

        return render(request, 'registro.html', {'form':form })
            








