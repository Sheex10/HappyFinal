from django.urls import path
from ApUno import views
from .views import home, Gatos, Perros, buscar_interno_producto, CamaPerro, formProductos, Agregar, InicioSesion, EditProducto, pruebaEDIT,ControlProd, Register, formRegistro, eliminarProd, EditProd2, ModiProd, Razas, InSesion, VerPerfil, homeJefe, RecuperarContra, Carrito, ModiPerfil, FormPerfilXD

urlpatterns = [
    path('', home,name="home"),
    path('Gatos', Gatos,name="Gatos"),
    path('Perros', Perros,name="Perros"),
    path('buscar_interno_producto/<int:id>',buscar_interno_producto,name="buscar_interno_producto"),
    path('Cama',CamaPerro,name="CamaPerro"),
    path('formProductos',formProductos, name="formProductos"),
    path('Agregar',Agregar,name="Agregar"),
    path('InicioSesion',InicioSesion,name="InicioSesion"),
    path('EditProducto',EditProducto,name="EditProducto"),
    path('pruebaEDIT',pruebaEDIT,name="pruebaEDIT"),
    path('ControlProd',ControlProd,name="ControlProd"),
    path('home', views.home, name='home'),
    path('homeJefe', homeJefe, name='homeJefe'),
    path('Registrarse',Register,name="Register"),
    path('formRegistro',formRegistro,name="formRegistro"),
    path('eliminarProd/<int:id>',eliminarProd,name="eliminarProd"),
    path('EditProd2/<int:id>',EditProd2,name="EditProd2"),
    path('ModiProd',ModiProd,name="ModiProd"),
    path('razas',Razas, name="Razas"),
    path('InSesion',InSesion,name="InSesion"),
    path('VerPerfil',VerPerfil,name="VerPerfil"),
    path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    path('carrito',Carrito,name="Carrito"),
    path('ModiPerfil',ModiPerfil,name="ModiPerfil"),
    path('FormPerfilXD',FormPerfilXD,name="FormPerfilXD"),


]
