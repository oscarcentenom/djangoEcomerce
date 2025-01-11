from django.contrib import admin
from ArticuloApp.models import Categoria, Producto, Tipo_NU, ImagenesSegundarias

# Register your models here.

class ImagenesSegundariasAdmin(admin.TabularInline):
    model = ImagenesSegundarias

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre_prod","ref_prod","descripcion_prod","tipo_prod")
    search_fields=("nombre_prod","descripcion_prod")
    list_filter=("categoria_prod",) 
    inlines = [
        ImagenesSegundariasAdmin,
        ]
       
    #readonly_fields=("created","updated")
    
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Tipo_NU)
