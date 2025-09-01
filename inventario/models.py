from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class MovimientoStock(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=50)  # e.g., 'entrada', 'salida'
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.producto_id.nombre} - {self.cantidad}"
    