from rest_framework import serializers
from .models import ServicioAdicional

class ServicioAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioAdicional
        fields = '__all__'