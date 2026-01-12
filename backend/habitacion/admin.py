from django.contrib import admin
from .models import Habitacion

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'numero_habitacion',
        'piso',
        'categoria',
        'condicion',
        'estado',
        'precio_base',
        'activa'
    ]
    
    list_editable = [
        'estado',
        'precio_base',
        'activa'
    ]
    
    fields = [
        'numero_habitacion',
        'piso',
        'tipo_ocupacion',
        'tamaño_cama',
        'categoria',
        'caracteristicas',
        'descripcion',
        'condicion',
        'estado',
        'precio_base',
        'activa'
    ]
    
    readonly_fields = ['condicion']
    list_filter = ['piso', 'categoria', 'estado', 'activa']
    search_fields = ['numero_habitacion']
    ordering = ['piso', 'numero_habitacion']