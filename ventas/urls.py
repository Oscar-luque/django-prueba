from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('clientes/', views.lista_clientes, name='listado_cliente'),
    path('clientes/nuevo/', views.crear_cliente, name='formulario_cliente'),
    path('clientes/crear_venta/<int:cliente_id>/', views.crear_venta, name='crear_venta'),
    path('', views.listado_ventas, name='listado_ventas'),
    path('clientes/eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
]