from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('productos', productos, name="productos"),
    path('vercompras', vercompras, name="vercompras"),
    path('suscripciones', suscripciones, name="suscripciones"),
    path('registro', registro, name="registro"),
    path('crudProducto', crudProducto, name="crudProducto"),
    path('crudPromociones', crudPromociones, name="crudPromociones"),
    path('pagar', pagar, name="pagar"),
    path('pagar2', pagar2, name="pagar2"),
    path('pagar3', pagar3, name="pagar3"),
    path('pagar4', pagar4, name="pagar4"),
    path('problemasPedido', problemasPedido, name="problemasPedido"),
    path('nosotros', nosotros, name="nosotros"),
    path('crearProducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    path('terminosycondiciones', terminosycondiciones, name="terminosycondiciones"),
    path('crearPromociones', crearPromociones, name="crearPromociones"),
    path('modificarPromociones/<id>', modificarPromociones, name="modificarPromociones"),
    path('eliminarPromociones/<id>', eliminarPromociones, name="eliminarPromociones"),
    
    

    
    
]
