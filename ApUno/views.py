from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'ApUno/home.html')

def Perros(request):
    return render(request, 'ApUno/Perros.html')

def Gatos(request):
    return render(request, 'ApUno/Gatos.html')

