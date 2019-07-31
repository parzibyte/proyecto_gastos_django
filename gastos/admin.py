from django.contrib import admin
from .models import Gasto # Importar nuestro modelo
# Register your models here.

# Registrarlo dentro de admin:
admin.site.register(Gasto)
