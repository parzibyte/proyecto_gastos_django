from django.db import models

# Create your models here.


class Gasto(models.Model):  # Extiende de models.Model
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
