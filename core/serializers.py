from rest_framework import serializers
from ApUno.models import Usuario

#clase de usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_admin','rut','nombre','apellido','direccion','tarjetas']