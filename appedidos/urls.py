
from django.urls import path
from .views import procesador_pedidos

urlpatterns = [
    path('', procesador_pedidos,name='Pedidos'),
]