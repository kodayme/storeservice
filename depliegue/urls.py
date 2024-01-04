"""
URL configuration for depliegue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# ESTAS SON LAS IMPORTACIONES PARA LOS ARCHIVOS MULTIMEDIA
from django.conf import settings
from django.conf.urls.static import static
# ========================================================

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apphome.urls')),
    path('services', include('appservicios.urls')),
    path('contenido', include('appcontenido.urls')),
    path('contactos', include('appcontacto.urls')),
    path('la_tienda', include('apptienda.urls')),
    path('carro', include('appcarro.urls')),
    path('registrar', include('appautenticacion.urls')),
    path('los_pedidos', include('appedidos.urls')),
]

# LA RUTA PARA LOS ARCHIVOS MEDIA
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)