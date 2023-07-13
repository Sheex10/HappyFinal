from django.shortcuts import render, redirect
from .models import Producto, Usuario, Categoria, Rol
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Vistas principales


def home(request):
    context = {}
    return render(request, 'ApUno/home.html', context)


def homeJefe(request):
    context = {}
    return render(request, 'ApUno/homeJefe.html', context)


def Perros(request):
    listaProductos = Producto.objects.filter(categoria=4)
    contexto = {
        "nomProd": listaProductos

    }
    return render(request, 'ApUno/Perros.html', contexto)


def Gatos(request):
    listaProductos = Producto.objects.filter(categoria=3)
    contexto = {
        "nomProd": listaProductos
    }
    return render(request, 'ApUno/Gatos.html', contexto)


def buscar_interno_producto(request, id):
    prod = Producto.objects.get(id_producto=id)
    contexto = {
        "nombree": prod
    }
    return render(request, 'ApUno/CamaPerro.html', contexto)

# Vistas para los productos


@login_required
def EditProducto(request):
    listaProductos = Producto.objects.all()
    contexto = {
        "nomProd": listaProductos

    }
    return render(request, 'ApUno/EditProducto.html', contexto)


def CamaPerro(request):

    return render(request, 'ApUno/CamaPerro.html')

# Esto es para cuando se agregue un producto.


@login_required
def formProductos(request):
    vIdProd = request.POST['id']
    vDescripcion = request.POST['desc']
    vPrecio = request.POST['precio']
    vFoto = request.FILES['foto']
    vCategoria = request.POST['categoria']
    vStock = request.POST['stock']
    vNombre = request.POST['nombre']
    vRegCategoria = Categoria.objects.get(id_categoria=vCategoria)

    Producto.objects.create(nombre=vNombre, id_producto=vIdProd, descripcion=vDescripcion,
                            precio=vPrecio, foto=vFoto, categoria=vRegCategoria, stock=vStock)

    if vRegCategoria.id_categoria == 4:
        return redirect('Perros')
    if vRegCategoria.id_categoria == 3:
        return redirect('Gatos')


@login_required
def Agregar(request):
    listaCategoria = Categoria.objects.all()
    contexto = {
        "Categorias": listaCategoria

    }
    return render(request, 'ApUno/Agregar.html', contexto)


@login_required(login_url='InicioSesion')
def VerPerfil(request):
    datUsuario = Usuario.objects.all()
    contexto = {
        "usuarios": datUsuario

    }
    return render(request, 'ApUno/VerPerfil.html', contexto)


def InicioSesion(request):
    logout(request)
    return render(request, 'ApUno/InicioSesion.html')


@login_required
def ControlProd(request):
    lista = Producto.objects.all()
    contexto = {
        "producto": lista
    }
    return render(request, 'ApUno/ControlProd.html', contexto)


def eliminarProd(request, id):
    producto = Producto.objects.get(id_producto=id)
    producto.delete()
    return redirect('EditProducto')

# ----------------


def EditProd2(request, id):
    TipoProd = Categoria.objects.all()
    producto = Producto.objects.get(id_producto=id)
    contexto = {
        "tipo_mascota": TipoProd,
        "prod": producto
    }
    return render(request, 'ApUno/EditProd2.html', contexto)

# ----------------


def ModiProd(request):
    vFotoProd = request.FILES.get('fotoProd', '')
    vIDProd = request.POST['idProd']
    vNombreProd = request.POST['nombreProd']
    vDescProd = request.POST['descripcionProd']
    vPrecioProd = request.POST['PrecioProd']
    vStockProd = request.POST['StockProd']
    vCategoriaProd = request.POST['categoriaProd']

    ProductoModi = Producto.objects.get(id_producto=vIDProd)
    ProductoModi.nombre = vNombreProd
    ProductoModi.descripcion = vDescProd
    ProductoModi.precio = vPrecioProd
    ProductoModi.stock = vStockProd

    registroCa = Categoria.objects.get(id_categoria=vCategoriaProd)
    ProductoModi.categoria = registroCa

    if vFotoProd != '':
        ProductoModi.foto = vFotoProd

    ProductoModi.save()
    messages.success(request, "Producto modificado.")
    return redirect('EditProducto')

# ----------------


def pruebaEDIT(request, id):
    prod = Producto.objects.all()
    produ = Producto.objects.get(codigoChip=id)
    contexto = {
        "lista_razas": prod,
        "datos": produ
    }
    return render(request, 'ApUno/pruebaEDIT.html', contexto)
# ----------------

# REGISTRO DE USUARIO


def Register(request):
    return render(request, 'ApUno/Register.html')


def RecuperarContra(request):
    return render(request, 'ApUno/RecuperarContra.html')


def formRegistro(request):
    vIdUser = request.POST['id_user']
    vNombre = request.POST['nomUser']
    vApellido = request.POST['apeUser']
    vClave = request.POST['Contrasena']
    vCorreo = request.POST['mailUser']
    vTelefono = request.POST['fonoUser']
    vRol = 2
    vRegistroRol = Rol.objects.get(nombreRol="usuario")
    print(f"aaaaaaaaaaa: {vRegistroRol}")
    valida = Usuario.objects.all()
    for xmail in valida:
        if xmail.correo == vCorreo:
            messages.error(request, "Este correo ya existe!")
            return redirect('Register')

    Usuario.objects.create(id_usuario= vIdUser,nombre=vNombre, apellido=vApellido, clave=vClave, correo=vCorreo,telefono=vTelefono, rol=vRegistroRol)
    user = User.objects.create_user(vCorreo, vCorreo, vClave)

    return redirect('InicioSesion')
# --------------------------


def Razas(request):
    return render(request, 'ApUno/Razas.html')
# PARA EL INICIO SESION


def InSesion(request):
    try:
        vCorreo = request.POST['correoUser']
        vClave = request.POST['password']
        vRol = 0
        vRun = 0
        registro = Usuario.objects.all()

        for i in registro:
            if i.correo == vCorreo and i.clave == vClave:

                vRun = i.id_usuario
                vRol = i.rol.id_rol
        user1 = User.objects.get(username=vCorreo)
        pass_valida = check_password(vClave, user1.password)

        if not pass_valida:
            messages.error(
                request, "El usuario o la contraseña son incorrectos")
            return redirect('InicioSesion')

        user = authenticate(username=vCorreo, password=vClave)

        if user is not None:
            if vRol == 2:
                login(request, user)
                return redirect('VerPerfil')

            if vRol == 1:
                login(request, user)
                return redirect('homeJefe')

            if vRol == 0:
                messages.success(request, "Usuario no registrado")
                return redirect('InicioSesion')
    except User.DoesNotExist:
        messages.error(request, "El usuario no existe")
        return redirect('InicioSesion')


def Carrito(request):
    return render(request, 'ApUno/Carrito.html')

@login_required
def ModiPerfil(request):
    datUsu = Usuario.objects.all()
    contexto = {
        "usuarios": datUsu
    }
    return render(request, 'ApUno/ModiPerfil.html', contexto)

@login_required(login_url='InicioSesion')
def FormPerfilXD(request):
    vNombreUser = request.POST['nomUser']
    vApellidoUser = request.POST['apeUser']
    vCorreoUser = request.POST['correoUser']
    vFonoUser = request.POST['fonoUser']

    correoU = request.user.username
    FormPerfilXD = Usuario.objects.get(correo=correoU)

    FormPerfilXD.nombre = vNombreUser
    FormPerfilXD.apellido = vApellidoUser
    FormPerfilXD.correo = vCorreoUser
    FormPerfilXD.telefono = vFonoUser
    FormPerfilXD.save()
    messages.success(request, "Perfil Modificado!.")

    return redirect('VerPerfil')
