# salon_eventos/serializers.py

from rest_framework import serializers
from .models import SalonEvento
# 💥 ¡CORRECCIÓN! Importar validadores estándar de Django, no de DRF
from django.core.validators import MinValueValidator 


class SalonEventoSerializer(serializers.ModelSerializer):
    
    # 1. Definir el campo explícitamente para añadir validadores
    capacidad = serializers.IntegerField(
        validators=[
            # 2. Usar MinValueValidator importado de django.core.validators
            MinValueValidator(0, message="La capacidad no puede ser un número negativo."),
        ]
    )

    class Meta:
        model = SalonEvento
        fields = '__all__'