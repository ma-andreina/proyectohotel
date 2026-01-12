# restaurante_mesa/serializers.py (Versión Limpia y Actualizada)

from rest_framework import serializers
from .models import RestauranteMesa 
from django.core.validators import MinValueValidator 

class RestauranteMesaSerializer(serializers.ModelSerializer):
    
    # 1. Validación para CAPACIDAD (Evita números < 1)
    capacidad = serializers.IntegerField(
        validators=[
            MinValueValidator(1, message="La capacidad de la mesa debe ser al menos 1 persona.")
        ]
    )
    
    # Nota: Los campos 'estado' y 'activa' se heredan directamente del modelo.
    # El parche 'numero_mesa_display' y 'disponible' han sido eliminados.
    
    class Meta:
        model = RestauranteMesa
        #  ACTUALIZACIÓN: Lista de campos limpios y nuevos
        fields = ('id','numero_mesa','capacidad', 'ubicacion', 'estado', 'activa')
              
     