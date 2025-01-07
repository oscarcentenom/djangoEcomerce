from django.contrib import admin
from ArticuloApp.models import Categoria, Producto, Tipo_NU

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre_prod","ref_prod","descripcion_prod","tipo_prod")
    search_fields=("nombre_prod","descripcion_prod")
    list_filter=("categoria_prod",) 
       
    #readonly_fields=("created","updated")
    
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Tipo_NU)
