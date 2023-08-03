from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html", )

def consolas(request):
    ctx = {'consolas': Consola.objects.all()}
    return render(request, "aplicacion/consolas.html", ctx)

def juegos(request):
    ctx = {'juegos': Juego.objects.all()}
    return render(request, "aplicacion/juegos.html", ctx)

def clientes(request):
    ctx = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", ctx)

def consolaForm(request):
    if request.method == "POST":
        miForm = ConsolaForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            consola = Consola(nombre=informacion['nombre'], compania=informacion['compania'], precio=informacion['precio'])
            consola.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = ConsolaForm()
    return render(request, "aplicacion/consolaForm.html", {"form":miForm})

def juegoForm(request):
    if request.method == "POST":
        miForm = JuegoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            juego = Juego(nombre=informacion['nombre'], genero=informacion['genero'], desarrollaora=informacion['desarrolladora'], precio=informacion['precio'])
            juego.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = JuegoForm()
    return render(request, "aplicacion/juegoForm.html", {"form":miForm})

def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            cliente.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = ClienteForm()
    return render(request, "aplicacion/clienteForm.html", {"form":miForm})

def buscarGenero(request):
    return render(request, "aplicacion/buscarGenero.html")

def buscar(request):
    if request.GET['genero']:
        genero = request.GET['genero']
        juego = Juego.objects.filter(genero__icontains= genero)
        return render(request,
                      "aplicacion/resultadosGenero.html", 
                      {"genero": genero, "juego": juego})
    return HttpResponse("No se ingresaron datos para buscar")