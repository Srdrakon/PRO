from django.contrib import admin # type: ignore

from .models import CustomUser, Producto
admin.site.register(CustomUser)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock')
    search_fields = ('nombre', 'descripcion')