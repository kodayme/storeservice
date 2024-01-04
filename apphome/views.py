from django.shortcuts import render
# from appcarro.appcart import Carro_de_compra
# Create your views here.

def home(request):

    # variable_carro = Carro_de_compra(request)

    return render(request,"home.html")