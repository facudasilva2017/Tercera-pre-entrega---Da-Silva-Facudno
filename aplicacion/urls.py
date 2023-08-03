from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="Inicio"),

    path('consolas/', consolas, name='consolas'),
    path('juegos/', juegos, name='juegos'),
    path('clientes/', clientes, name='clientes'),

    path('consola_form/', consolaForm, name='consola_form'),
    path('juego_form/', juegoForm, name='juego_form'),
    path('cliente_form/', clienteForm, name='cliente_form'),

    path('buscar_genero/', buscarGenero, name='buscar_genero'),
    path('buscar/', buscar, name='buscar')
]