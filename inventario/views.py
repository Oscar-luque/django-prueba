from django.shortcuts import render, get_object_or_404
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

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('inventario:productos_disponibles')
    return render(request, 'inventario/formulario_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('inventario:productos_disponibles')
    return render(request, 'inventario/confirmar_eliminar.html', {'producto': producto})

def index_view(request):
    return render(request, 'base.html')