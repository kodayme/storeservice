from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return  self.nombre

class Contenido(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    categoria = models.ManyToManyField(Categoria)
    imagen = models.ImageField(upload_to="contenido", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'contenido'
        verbose_name_plural = 'contenidos'

    def __str__(self):
        return  self.titulo










