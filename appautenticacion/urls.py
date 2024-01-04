
from django.urls import path
from .views import loguear,sierre_de_session,inicio_sesion

# CLASE 64
urlpatterns = [
    path('/', loguear.as_view(),name='sighnin'),
    path('', sierre_de_session,name='logout'),
    path('inicio_sesion', inicio_sesion,name='login'),
]