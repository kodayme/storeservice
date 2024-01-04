from django.shortcuts import render
from .models import *
# Create your views here.

def contenido(request):
    contenidos = Contenido.objects.all()
    return render(request,"contenido.html",{"los_contenidos":contenidos})

def las_categorias(request, categoria_id):

    kategoria = Categoria.objects.get(id=categoria_id)

    contenidos = Contenido.objects.filter(categoria=kategoria)

    return render(request, "categorias.html", {"categoria":kategoria, "los_contenidos":contenidos})
