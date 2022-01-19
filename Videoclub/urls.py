from django.urls import path
from Videoclub import views
urlpatterns = [
    path('index/', views.index),
    path('formularioPeliculas/', views.formulario_peliculas),
    path('listadoPeliculas/', views.listado_peliculas),
    path('confirmacionAlta/', views.alta_pelicula),
]