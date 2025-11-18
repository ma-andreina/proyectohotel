from rest_framework import serializers
from .models import ReservaServicio

class ReservaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaServicio
        fields = '__all__'