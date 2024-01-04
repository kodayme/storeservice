from django.contrib import admin
from django.urls import path
from .views import Contacto

urlpatterns = [
    path('', Contacto,name='contact'),#OJO LA BARRA SLASH '/' ES PARA IDENTIFICAR LA RUTA AL REDIRECCIONAR LA PÁGINA
]