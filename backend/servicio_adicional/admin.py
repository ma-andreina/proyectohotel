from django.contrib import admin
from .models import ServicioAdicional


@admin.register(ServicioAdicional)
class ServicioAdicionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio')
