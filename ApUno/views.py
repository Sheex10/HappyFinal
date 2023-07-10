from django.shortcuts import render, redirect
from .models import Producto, Usuario, Categoria, Rol
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

#Vistas principales

def home(request):
    context={}
    return render(request, 'ApUno/home.html',context)

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
@login_required
def EditProducto(request):
    listaProductos = Producto.objects.filter(categoria = 4)
    contexto={
        "nomProd": listaProductos

    }
    return render(request,'ApUno/EditProducto.html',contexto)

def CamaPerro(request):
   
    return render(request, 'ApUno/CamaPerro.html')

#Esto es para cuando se agregue un producto.
@login_required
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
@login_required    
def Agregar(request):
    listaCategoria=Categoria.objects.all()
    contexto={
        "Categorias":listaCategoria

    }
    return render(request, 'ApUno/Agregar.html', contexto)

def InicioSesion(request):
    return render(request, 'ApUno/InicioSesion.html')

@login_required
def ControlProd(request):
 lista= Producto.objects.all()
 contexto = {
    "producto": lista
 }
 return render(request, 'ApUno/ControlProd.html',contexto)

def eliminarProd (request):
    producto = Producto.objects.get()
    producto.delete()
    return redirect('lista')

#----------------
def pruebaEDIT(request, id):
    prod = Producto.objects.all()
    produ = Producto.objects.get(codigoChip = id)
    contexto = {
        "lista_razas": prod,
        "datos": produ
    }
    return render(request, 'ApUno/pruebaEDIT.html', contexto)
#----------------

# REGISTRO DE USUARIO
def Register(request):
    return render(request,'ApUno/Register.html')

def formRegistro(request):
    vNombre = request.POST['nomUser']
    vApellido = request.POST['apeUser']
    vClave = request.POST['Contraseña']
    vCorreo = request.POST['mailUser']
    vTelefono = request.POST['fonoUser']
    vRol = 1
    vRegistroRol = Rol.objects.get(id_rol=vRol)

    valida = Usuario.objects.all()
    for xmail in valida:
        if xmail.correo == vCorreo:
            messages.error(request,"Este correo ya existe!")
            return redirect('Register')
    
    Usuario.objects.create(nombre=vNombre, apellido=vApellido, clave=vClave, correo=vCorreo, 
                           telefono=vTelefono, rol=vRegistroRol)
    user = User.objects.create_user(vCorreo,vCorreo,vClave)

    return redirect('Login')
#--------------------------

