from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class META:
        verbose_name = "la_categoria"
        verbose_name_plural = "las_categorias"

    def __str__(self):
        return self.nombre

class Artiulos(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class META:
        verbose_name = "el_articulo"
        verbose_name_plural = "los_articulos"
    def __str__(self):
        return self.nombre



