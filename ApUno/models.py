from django.db import models

# Create your models here.

class Rol(models.Model):
    id_rol=models.IntegerField(primary_key=True, verbose_name="id de rol")
    nombreRol=models.CharField(max_length=30, verbose_name="nombre del rol")
    
    def __str__(self):
        return self.nombreRol
#-----------------------------------

class Usuario(models.Model):
    id_usuario =models.IntegerField(primary_key=True, verbose_name="id del usuario")
    nombre=models.CharField(max_length=20, verbose_name="nombre del usuario")
    apellido=models.CharField(max_length=20, verbose_name="apellido usuario")
    correo=models.CharField(max_length=50, verbose_name="correo usuario")
    clave=models.CharField(max_length=12, verbose_name="clave usuario")
    telefono=models.IntegerField(verbose_name="telefono usuario")
    rol =models.ForeignKey(Rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.correo
#--------------------------------------
class Venta(models.Model):
    id_venta =models.IntegerField(primary_key=True, verbose_name="id de venta")
    f_venta = models.DateField()
    r_envio=models.CharField(max_length=500, verbose_name="registro del envio")
    costo_envio=models.IntegerField(verbose_name="costo envío")
    total = models.IntegerField()
    carrito = models.IntegerField(verbose_name="1-Carrito - 0- Venta")
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.r_envio

#----------------------------------
class Categoria(models.Model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name="id de rol")
    nombre=models.CharField(max_length=30, verbose_name="nombre de categoria")
    
    def __str__(self):
        return self.nombre
#--------------------------------------
class Producto(models.Model):
    id_producto =models.IntegerField(primary_key=True, verbose_name="id del producto")
    nombre=models.CharField(max_length=30, verbose_name="nombre del producto")
    descripcion=models.CharField(max_length=700, verbose_name="descripcion producto")
    precio=models.IntegerField(verbose_name="precio producto")
    stock = models.IntegerField()
    foto=models.ImageField(upload_to="foto producto")
    categoria =models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
#-------------------------------------


class Region(models.Model):
    id_region=models.IntegerField(primary_key=True, verbose_name="id de region")
    nombre=models.CharField(max_length=30, verbose_name="nombre de region")
    
    def __str__(self):
        return self.nombre
 #-----------------------------------       
class Comuna(models.Model):
    id_comuna =models.IntegerField(primary_key=True, verbose_name="id de comuna")
    nombre=models.CharField(max_length=20, verbose_name="nombre comuna")
    costo_despacho=models.IntegerField(verbose_name="costo del despacho")
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
#-----------------------------------

class Direccion(models.Model):
    id_direccion =models.IntegerField(primary_key=True, verbose_name="id de direccion")
    calle=models.CharField(max_length=100, verbose_name="nombre calle")
    numero=models.IntegerField(verbose_name="numero casa")
    descripcion=models.CharField(max_length=600, verbose_name="descripcion direccion")
    comuna =models.ForeignKey(Comuna, models.CASCADE)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion
#-------------------------------------


class Detalle(models.Model):
    id_detalle =models.IntegerField(primary_key=True, verbose_name="id de detalle")
    cantidad=models.IntegerField(verbose_name="cantidad")
    subtotal = models.IntegerField(verbose_name="subtotal de venta")
    venta=models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    
#Fin Modelos!