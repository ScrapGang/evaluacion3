from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto','marcaProducto','stockProducto','precioProducto']

class PromocionesForm(ModelForm):
    class Meta:
        model = Promociones
        fields = ['idPromociones','nombrePromociones','marcaPromociones','stockPromociones','precioPromociones','descuentoPromociones','fechainiPromociones','fechaterPromociones','preciofinPromociones']


        