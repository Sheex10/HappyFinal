from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from ApUno.models import Usuario, Venta
from .serializers import UsuarioSerializers

# Create your views here.


@csrf_exempt
@api_view(['GET','POST'])
def lista_usuario(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializers(usuario,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_usuario(request, id):
    """

    Get, update, o delete de un usuario en particular
    """
    try:
        usuario = Usuario.objects.get(id_admin=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Usuario.Serializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        date = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.os_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)

