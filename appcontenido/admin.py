from django.contrib import admin
from .models import Categoria,Contenido

# Register your models here.

class categoriaadmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class contenidoadmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Categoria,categoriaadmin)
admin.site.register(Contenido,contenidoadmin)

