from django.urls import path
from .views import home, Gatos, Perros

urlpatterns = [
    path('', home,name="home"),
    path('Gatos', Gatos,name="Gatos"),
    path('Perros', Perros,name="Perros"),
]
