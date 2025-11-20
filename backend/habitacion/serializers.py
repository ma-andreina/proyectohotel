from rest_framework import serializers
from .models import Habitacion  # Ajusta según tu modelo

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'  # Incluye todos los campos del modelo