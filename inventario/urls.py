from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('productos/', views.productos_disponibles, name='productos_disponibles'),
    path('crear/', views.crear_producto, name='crear_producto'),
]