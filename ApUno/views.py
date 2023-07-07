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

def EditProducto(request):
    listaProductos = Producto.objects.filter(categoria = 4)
    contexto={
        "nomProd": listaProductos

    }
    return render(request,'ApUno/EditProducto.html',contexto)

def CamaPerro(request):
   
    return render(request, 'ApUno/CamaPerro.html')

#Esto es para cuando se agregue un producto.

def formProductos(request):
    vIdProd= request.POST['id']
    vDescripcion= request.POST['desc']
    vPrecio= request.POST['precio']
    vFoto=request.FILES['foto']
    vCategoria=request.POST['categoria']
    vStock=request.POST['stock']
    vNombre=request.POST['nombre']
    vRegCategoria=Categoria.objects.get(id_categoria=vCategoria)

    Producto.objects.create(nombre=vNombre, id_producto=vIdProd, descripcion=vDescripcion,  precio=vPrecio, foto=vFoto, categoria=vRegCategoria, stock=vStock)

    if vRegCategoria.id_categoria==4:
        return redirect('Perros')
    if vRegCategoria.id_categoria==3:
        return redirect('Gatos')
    
def Agregar(request):
    listaCategoria=Categoria.objects.all()
    contexto={
        "Categorias":listaCategoria

    }
    return render(request, 'ApUno/Agregar.html', contexto)

def InicioSesion(request):
    return render(request, 'ApUno/InicioSesion.html')

#----------------
def pruebaEDIT(request):
   
    return render(request, 'ApUno/pruebaEDIT.html')
#----------------