from django.shortcuts import render, redirect
from .models import Producto, Usuario, Categoria
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

#Vistas principales

def home(request):
    return render(request, 'ApUno/home.html')

def Perros(request):
    listaProductos = Producto.objects.filter(categoria = 4)
    contexto={
        "nomProd": listaProductos

    }
    return render(request,'ApUno/Perros.html', contexto)

def Gatos(request):
    listaProductos = Producto.objects.filter(categoria = 3)
    contexto={
        "nomProd": listaProductos
    }
    return render(request, 'ApUno/Gatos.html', contexto)

def buscar_interno_producto(request,id):
    prod = Producto.objects.get(id_producto = id)
    contexto = {
        "nombree": prod
    }
    return render(request,'ApUno/CamaPerro.html',contexto)

#Vistas para los productos

def CamaPerro(request):
    nombreC = "Cama antiestres"
    precioC = "PRECIO : $30.990"
    descripcionC = "La cama antiestrés -100-120cm- Damasco disponibles en diferentes tamaños.Esta cama calmante tiene un tejido especial de suave felpa, para que tu mascota esté comoda y relajada."

    contexto = {
        "nombre" : nombreC,
        "precio" : precioC,
        "descripcion" : descripcionC
    }
    return render(request, 'ApUno/CamaPerro.html', contexto)