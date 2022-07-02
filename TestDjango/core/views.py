from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from .models import *
from .forms import ProductoForm
from .forms import PromocionesForm


# Create your views here.
def home(request):
    
    return render(request, 'core/home.html')

def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    return render(request, 'core/registro.html', {'form':form})


def crearProducto(request):
    datos = {"form":ProductoForm()}
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto agregado!."
    return render(request, 'core/crearProducto.html', datos)

def crearPromociones(request):
    datos = {"form":PromocionesForm()}
    if request.method == "POST":
        form = PromocionesForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Promoción agregado!."
    return render(request, 'core/crearPromociones.html', datos)

def modificarPromociones(request, id):
    promociones = Promociones.objects.get(idPromociones=id)
    datos = {'form': PromocionesForm(instance=promociones)}
    if request.method == "POST":
        form = PromocionesForm(request.POST, instance=promociones)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/modificarPromociones.html', datos)

def eliminarPromociones(request, id):
    promociones = Promociones.objects.get(idPromociones=id)
    promociones.delete()
    return redirect(to = "crudPromociones")

def modificarProducto(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos = {'form': ProductoForm(instance=producto)}
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/modificarProducto.html', datos)

def eliminarProducto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(to = "crudProducto")

def crudProducto(request):
    productos= Producto.objects.all()
    return render(request, 'core/crudProducto.html', {'contexto':productos})

def crudPromociones(request):
    promociones= Promociones.objects.all()
    return render(request, 'core/crudPromociones.html', {'contexto':promociones})  

def pagar(request):
    return render(request, 'core/pagar.html')

def pagar2(request):
    return render(request, 'core/pagar2.html')

def pagar3(request):
    return render(request, 'core/pagar3.html')

def pagar4(request):
    return render(request, 'core/pagar4.html')

def problemasPedido(request):
    return render(request, 'core/problemasPedido.html')  

def nosotros(request):
    return render(request, 'core/nosotros.html')

def terminosycondiciones(request):
    return render(request, 'core/terminosycondiciones.html')
    


def productos(request):
    return render(request, 'core/productos.html')

def vercompras(request):
    return render(request, 'core/vercompras.html')

def suscripciones(request):
    return render(request, 'core/suscripciones.html')

