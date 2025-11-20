from rest_framework import serializers
from .models import ReservaRestaurante

class ReservaRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaRestaurante
        fields = '__all__'