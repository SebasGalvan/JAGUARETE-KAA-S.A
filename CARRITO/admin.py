from CARRITO.models import Carrito, Categoria, Producto
from django.contrib import admin


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito)
