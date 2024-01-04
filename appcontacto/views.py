from django.shortcuts import render, redirect
from .forms import formulario
# Create your views here.

from django.core.mail import EmailMessage

def Contacto(request):

    variable_formulario = formulario()

    if request.method=="POST":

        variable_formulario = formulario(data=request.POST)

        if variable_formulario.is_valid():

            nombre = request.POST.get("nombre")
            correo = request.POST.get("correo")
            consulta = request.POST.get("Consultas_Y_Preguntas")

            correo = EmailMessage("Mensaje recibido de tu página",
                                  "el usuario {} cuya dirección {} pregunta lo envía lo siguiente: {}".format(nombre,correo,consulta),
                                  "",["pietroblaster@gmail.com"],reply_to=[correo])

            try:
                correo.send()

                return redirect("/contactos/?mensaje")#OJO ESTA RUTA ES LA QUE VÁ EN EL URL PRINCIPAL
            except:
                return redirect("/contactos/?correo_inválido")

    return render(request,"contacto.html",{"contacto":variable_formulario})
