from django import forms
from .models import Cliente, ItemVenta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre']

class ItemVentaForm(forms.ModelForm):
    class Meta:
        model = ItemVenta
        fields = ['producto', 'cantidad', 'precio_unitario']