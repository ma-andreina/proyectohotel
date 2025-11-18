from rest_framework import serializers
from .models import ReservaHabitacion

class ReservaHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaHabitacion
        fields = '__all__'