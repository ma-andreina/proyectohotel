from rest_framework import serializers
from .models import SalonEvento

class SalonEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonEvento
        fields = '__all__'