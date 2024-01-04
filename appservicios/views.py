from django.shortcuts import render
from .models import Servicio
# Create your views here.

def los_servicios(request):
    service = Servicio.objects.all()
    return render(request,"servicio.html",{'servis':service})
