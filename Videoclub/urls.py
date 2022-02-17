from django.urls import path
from Videoclub.views import register
from Videoclub import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',views.inicio, name="inicio"),
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
    path('about/',views.about),

    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout')
   
]
#Para imágenes
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)