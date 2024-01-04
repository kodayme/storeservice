from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import fomulario_usuario
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

class loguear(View):

    def get(self, request):
        form = fomulario_usuario()
        return render(request,"registro.html", {"formulario":form})


    def post(self, request):
        form = fomulario_usuario(request.POST)

        if form.is_valid():

            usuario = form.save()

            login(request,usuario)

            return redirect('Home')

        else:
            for item in form.error_messages:
                messages.error(request, form.error_messages[item])

            return render(request,"registro.html", {"formulario":form})

def sierre_de_session(request):
    logout(request)
    return redirect('Home')

def inicio_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=clave)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request,"usuario inválido")
        else:
            messages.error(request, "datos inválidos")
    form = AuthenticationForm()
    return render(request,"inicio.html", {"fomulario_inicio":form})