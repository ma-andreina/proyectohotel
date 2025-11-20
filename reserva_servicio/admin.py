from django.contrib import admin
from .models import ReservaServicio


@admin.register(ReservaServicio)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva_habitacion_id', 'servicio_id')
