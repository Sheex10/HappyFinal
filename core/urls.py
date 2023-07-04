from django.urls import path,include
from core.views import lista_usuario, detalle_usuario

urlpatterns = [
    path('lista_usuario',lista_usuario,name="lista_usuario"),
    path('detalle_usuario/<id>',detalle_usuario,name="detalle_usuario"),
]