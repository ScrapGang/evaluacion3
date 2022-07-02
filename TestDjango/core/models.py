from django.db import models

# Create your models here.
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    marcaProducto = models.CharField(max_length=20)
    stockProducto = models.CharField(max_length=20)
    precioProducto = models.CharField(max_length=20)

    

class Promociones(models.Model):
    idPromociones = models.IntegerField(primary_key=True)
    nombrePromociones = models.CharField(max_length=50)
    marcaPromociones = models.CharField(max_length=20)
    stockPromociones = models.CharField(max_length=20)
    precioPromociones = models.CharField(max_length=20)
    descuentoPromociones = models.CharField(max_length=20)
    fechainiPromociones = models.CharField(max_length=10)
    fechaterPromociones = models.CharField(max_length=10)
    preciofinPromociones = models.CharField(max_length=20)

   

   