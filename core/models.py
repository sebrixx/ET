from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=80, blank=True)
    detalle = models.CharField(max_length=450)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=200)
    oferta = models.BooleanField()
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE)
    porcentaje_oferta = models.IntegerField(default=0)
    
    def tachado(self):
        if self.oferta:
            return "$" + str(round(self.precio / (1 - (self.porcentaje_oferta / 100))))
        return ""

    def descuento(self):
        if self.oferta:
            return str(self.porcentaje_oferta) + "% Dcto."
        return ""

    def __str__(self):
        return self.codigo+" "+self.nombre


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    estado_envio = models.CharField(max_length=15, default="EN PREPARACION")
    total = models.IntegerField()
    
    def __str__(self):
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)[0:16]
    
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField() 
    
    def __str__(self):
        return str(self.id) + " " + self.producto.nombre[0:20] + " " + str(self.venta.id)
    

    