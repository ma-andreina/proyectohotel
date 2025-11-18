from django.contrib import admin
from .models import ReservaHabitacion


@admin.register(ReservaHabitacion)
class ReservaHabitacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_id', 'habitacion_id')
