from django.contrib import admin
from PedidosApp.models import Pedidos, DetallePedidos

# Register your models here.
admin.site.register(Pedidos)
admin.site.register(DetallePedidos)