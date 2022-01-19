
from django.contrib import admin
from django.urls import path, include
from Videoclub.views import index
from Videoclub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Videoclub/',include('Videoclub.urls')),
    path('listadoPeliculas/', views.listado_peliculas),
    path('ConfirmacionAlta/', views.alta_pelicula)
    
   
]
