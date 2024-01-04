from django.urls import path

from . import views
app_name = "carro"

urlpatterns = [


    path("agregar/<int:producto_id>/", views.agregador_de_productos, name="agrega"),
    path("eliminar/<int:producto_id>/", views.removedor_de_productos, name="delete"),
    path("restar/<int:producto_id>/", views.resta_productos, name="resta"),
    path("limpiar/<int:producto_id>/", views.limpia_carro, name="clear"),

]