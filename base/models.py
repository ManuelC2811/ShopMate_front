from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    
    CATEGORY = (
    ('alimentos', 'Alimentos'),
    ('limpieza', 'Limpieza'),
    ('ropa', 'Ropa'),
    ('electrónicos', 'Electrónicos'),
    ('hogar', 'Hogar'),
    ('belleza', 'Belleza'),
    ('juguetes', 'Juguetes'),
    ('otros', 'Otros'),
    )   
    UNIT = (
        ('un', 'Unidad'),
        ('paquete', 'Paquete'),
        ('kg', 'Kilos'),
        ('lb', 'Libras'),
        ('lt', 'Litros'),
    )
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveBigIntegerField(null=False)
    unidad = models.CharField(max_length=200, null=False, choices=UNIT)
    cantidad = models.PositiveSmallIntegerField(null=False)
    categoria = models.CharField(max_length=200, null=False, choices=CATEGORY)
    comprado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nombre

    class Meta:
        order_with_respect_to = 'user'
