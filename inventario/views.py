from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import redirect
# Create your views here.
def productos_disponibles(request):
    productos = Producto.objects.filter(stock__gt=0)
    return render(request, 'inventario/productos.html', {'productos': productos})

def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventario:productos_disponibles')
    return render(request, 'inventario/formulario_producto.html', {'form': form})