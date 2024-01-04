from django.urls import path
from . import views


urlpatterns = [
    path('', views.contenido,name='Contenidos'),
    path('categoria/<int:categoria_id>/', views.las_categorias, name="categorias"),
]