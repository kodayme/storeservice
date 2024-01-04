def importe_total_carro(request):
    total = 0
    if "carrito" in request.session:
        if request.user.is_authenticated:
            for key, value in request.session["carrito"].items():
                total = total+float(value["precio"])
    return {"importe_total_carro":total}


# OJO MUY IMPORTANTE: DESPUÉS DE HABER CREADO LA VARIABLE CON EN NOMBRE DE "context_processor.py", DE DEBE DE REGISTRAR
# EN EL SETTINGS EN EL CAMPO DE 'TEMPLATES' CON SU RUTA. EJEMPLO: 'appcarro.context_processor.importe_total_carro'

