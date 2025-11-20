from django.contrib import admin
from .models import Habitacion


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_habitacion', 'categoria')
