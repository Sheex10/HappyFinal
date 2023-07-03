from django.shortcuts import render, redirect
from .models import Producto, Usuario, Categoria

# Create your views here.

def home(request):
    return render(request, 'ApUno/home.html')

def Perros(request):
    listaProductos = Producto.objects.filter(categoria = 4)
    contexto={
        "nomProd": listaProductos

    }
    return render(request,'ApUno/Perros.html', contexto)

def Gatos(request):
    return render(request, 'ApUno/Gatos.html')

def buscar_interno_producto(request,id):
    prod = Producto.objects.get(id_producto = id)
    contexto = {
        "nombree": prod
    }
    return render(request,'ApUno/Correa.html',contexto)