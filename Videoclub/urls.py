from django.urls import path
from .views import index
from Videoclub import views
urlpatterns = [
    path('index/', views.index),
    #path('listado_peliculas', index ),
    path('formularioPeliculas/', views.formulario_peliculas),
    path('listadoPeliculas/', views.listado_peliculas),
]