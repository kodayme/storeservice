from django.shortcuts import render
from .models import Artiulos
# Create your views here.

def Tienda(request):
    merca = Artiulos.objects.all()
    return render(request, "tienda.html",{"articulos":merca})
