from django.urls import path

from . import views # Importar views.py

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('hola', views.hola, name='hola'),
    path('agregar', views.agregar_gasto, name='agregar_gasto'),
]