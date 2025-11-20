from django.contrib import admin
from .models import TarifaDinamica


@admin.register(TarifaDinamica)
class TarifaDinamicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'habitacion_id', 'precio')
