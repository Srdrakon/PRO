# processes/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    rut = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Producto(models.Model):
    CODIGO_CHOICES = [
        (1, 'Presencial'),
        (2, 'Online'),
        (3, 'Ambas')
    ]

    DESPACHO_CHOICES = [
        (1, 'Sí'),
        (2, 'No')
    ]

    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    proveedor = models.CharField(max_length=200)
    stock = models.PositiveIntegerField()
    disponibilidad_venta = models.IntegerField(choices=CODIGO_CHOICES)
    disponibilidad_despacho = models.IntegerField(choices=DESPACHO_CHOICES)

    def __str__(self):
        return self.nombre