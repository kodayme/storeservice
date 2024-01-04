from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMessage
from django.shortcuts import render,redirect
from django.utils.html import strip_tags

from .models import Pedido,Linea_Pedido
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.
from appcarro.appcart import Carro_de_compra

from django.core.mail import EmailMessage

@login_required(login_url="/registrar/inicio_sesion")
def procesador_pedidos(request):
    pedido = Pedido.objects.create(usuario = request.user)
    variable_carro = Carro_de_compra(request)
    variable_lineas_de_pedido = list()

    for key, value in variable_carro.carrito.items():
        variable_lineas_de_pedido.append(Linea_Pedido(
            producto_id = key,
            cantidad = value["cantidad"],
            usuario = request.user,
            pedido = pedido

        ))

    Linea_Pedido.objects.bulk_create(variable_lineas_de_pedido)

    envio_de_email(pedido = pedido,
                   variable_lineas_de_pedido = variable_lineas_de_pedido,
                   nombre_usuario = request.user.username,
                   email_usuario = request.user.email)


    messages.success(request,"¡ Compra realizada correctamente!")
    return redirect("Home")

def envio_de_email(**kwargs):
    asunto = "¡Gracias por tu compra!"
    mensaje = render_to_string("pedido.html",{
        "pedido":kwargs.get("pedido"),
        "variable_lineas_de_pedido":kwargs.get("variable_lineas_de_pedido"),
        "nombre_usuario":kwargs.get("nombre_usuario"),
        "email_usuario":kwargs.get("email_usuario")
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "pietroblaster@gmail.com"
    to = kwargs.get("email_usuario")


    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)




