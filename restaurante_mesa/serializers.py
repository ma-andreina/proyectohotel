from rest_framework import serializers
from .models import RestauranteMesa

class RestauranteMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestauranteMesa
        fields = '__all__'