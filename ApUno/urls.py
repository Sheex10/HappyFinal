from django.urls import path
from .views import home, Gatos, Perros, buscar_interno_producto, CamaPerro, formProductos, Agregar, InicioSesion

urlpatterns = [
    path('', home,name="home"),
    path('Gatos', Gatos,name="Gatos"),
    path('Perros', Perros,name="Perros"),
    path('buscar_interno_producto/<int:id>',buscar_interno_producto,name="buscar_interno_producto"),
    path('Cama',CamaPerro,name="CamaPerro"),
    path('formProductos',formProductos, name="formProductos"),
    path('Agregar',Agregar,name="Agregar"),
    path('InicioSesion',InicioSesion,name="InicioSesion"),
]
