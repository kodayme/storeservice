from django.shortcuts import render,redirect
from .appcart import Carro_de_compra
from apptienda.models import Artiulos
# Create your views here.

def agregador_de_productos(request, producto_id):
    variable_carro = Carro_de_compra(request)
    variable_producto = Artiulos.objects.get(id= producto_id)

    variable_carro.agregar(variable_producto)
    return redirect("Store")

def removedor_de_productos(request, producto_id):
    segunda_variable_carro = Carro_de_compra(request)
    segunda_variable_producto = Artiulos.objects.get(id=producto_id)

    segunda_variable_carro.eliminar(segunda_variable_producto)
    return redirect("la_tienda")

def resta_productos(request, producto_id):
    tercera_variable_carro = Carro_de_compra(request)
    tercera_variable_producto = Artiulos.objects.get(id=producto_id)

    tercera_variable_carro.restar_producto(tercera_variable_producto)
    return redirect("Store")

def limpia_carro(request, producto_id):
    cuarta_variable_carro = Carro_de_compra(request)
    cuarta_variable_carro.limpiar_carro()
    return redirect("la_tienda")