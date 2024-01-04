from django.contrib import admin
from .models import Categoria, Artiulos
# Register your models here.

class admicategoria(admin.ModelAdmin):
    readonly_fields = ("created","updated")


class adminarticulos(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("disponibilidad",)

admin.site.register(Categoria, admicategoria)
admin.site.register(Artiulos,adminarticulos)
