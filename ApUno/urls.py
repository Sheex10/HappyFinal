from django.urls import path
from ApUno import views
from .views import home, Gatos, Perros, buscar_interno_producto, CamaPerro, formProductos, Agregar, InicioSesion, EditProducto, pruebaEDIT,ControlProd

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
]
