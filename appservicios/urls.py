
from django.urls import path
from .views import los_servicios

urlpatterns = [
    path('', los_servicios,name='servicios'),
]