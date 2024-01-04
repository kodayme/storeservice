from django.db import models
from django.contrib.auth import get_user_model
from apptienda.models import Artiulos
from django.db.models import F,Sum,FloatField

User = get_user_model()
# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    @property
    def total(self):
        return self.linea_pedido_set.aggregate(
            total = Sum(F("precio") *("cantidad"), output_field=FloatField())
        )["total"]

    def __str__(self):
        return self.id


    class Meta:
        db_table = 'pedido'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class Linea_Pedido(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    producto = models.ForeignKey(Artiulos, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'linea_pedido'
        verbose_name = 'linea_pedido'
        verbose_name_plural = 'lineas_pedidos'
        ordering = ['id']