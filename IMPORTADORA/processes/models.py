
# processes/models.py
# from django.db import models
# Create your models here.
# processes/models.py      

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


 ##########################################################################
    # IMPORTADORA MODELO DE USUARIOS
# processes/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
