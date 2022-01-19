from django.urls import path
from Videoclub import views
urlpatterns = [
    path('index/', views.index),
    path('formularioPeliculas/', views.formulario_peliculas),
    path('listadoPeliculas/', views.listado_peliculas),
    path('confirmacionAlta/', views.alta_pelicula),
    path('eliminarPelicula/<int:id>', views.eliminar_pelicula),
    path('formularioModificacion/<int:id>', views.formulario_modificacion),
    path('modificarPelicula/', views.modificar_pelicula),
    
]