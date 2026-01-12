# habitacion/serializers.py
from rest_framework import serializers
from .models import Habitacion


class HabitacionSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Habitacion.
    
    Proporciona serialización y deserialización para todas las operaciones
    CRUD de las habitaciones a través de la API REST.
    """
    
    class Meta:
        model = Habitacion
        fields = '__all__'