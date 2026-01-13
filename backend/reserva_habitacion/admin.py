# reserva_habitacion/admin.py

from django.contrib import admin
from .models import ReservaHabitacion
# Importar el modelo de la relación (Tabla Pivote)
from reserva_servicio.models import ServicioReserva 

# =========================================================
# 1. DEFINICIÓN DEL INLINE (Para mostrar los Servicios)
# =========================================================

class ServicioReservaInline(admin.TabularInline):
    """
    Permite editar los Servicios Adicionales dentro de la vista de ReservaHabitacion.
    """
    model = ServicioReserva
    extra = 1 # Muestra una línea vacía extra para añadir un nuevo servicio
    # Muestra los campos importantes de la relación
    fields = ('servicio', 'cantidad', 'precio_unitario') 
    readonly_fields = ('precio_unitario',) # El precio unitario debe ser fijo al crearse
    raw_id_fields = ('servicio',) # Usa una interfaz de búsqueda para la FK

# =========================================================
# 2. REGISTRO DEL MODELO PRINCIPAL CON EL INLINE
# =========================================================

@admin.register(ReservaHabitacion)
class ReservaHabitacionAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_confirmacion', 
        'usuario', 
        'habitacion', 
        'fecha_checkin', 
        'fecha_checkout', 
        'estado', 
        'total'
    )
    list_filter = ('estado', 'fecha_checkin')
    search_fields = ('codigo_confirmacion', 'usuario__username', 'habitacion__numero_habitacion')
    readonly_fields = ('codigo_confirmacion', 'fecha_creacion', 'total')
    raw_id_fields = ('usuario', 'habitacion')
    
    # 💡 ¡LA CORRECCIÓN ESTÁ AQUÍ! Se añade el inline.
    inlines = [ServicioReservaInline]