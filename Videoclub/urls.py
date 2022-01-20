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



    path('formularioSocio/', views.formulario_socio),
    path('confirmacionAltaSocio/', views.confirmacion_alta_socio),
    path('listadoSocios/', views.listado_socios),
    path('eliminarSocio/<int:id>', views.eliminar_socio),
    path('formularioModificacionSocio/<int:id>', views.formulario_modificacion_socio),
    path('modificarSocio/', views.modificar_socio),


    
    path('listadoEmpleados/', views.listado_empleados),
    path('formularioEmpleado/', views.formulario_empleado),
    path('confirmacionAltaEmpleado/', views.confirmacion_alta_empleado),
    path('formularioModificacionEmpleado/<int:id>', views.formulario_modificacion_empleado),
    path('modificarEmpleado/', views.modificar_empleado),
    path('eliminarEmpleado/<int:id>', views.eliminar_empleado),

    

    

    

    

    
    






    
]