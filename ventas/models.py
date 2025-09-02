from django.db import models
from inventario.models import Producto

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Venta de {self.producto} a {self.cliente.nombre}"
    
class ItemVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto} @ {self.precio_unitario}"

    def total(self):
        return self.cantidad * self.precio_unitario