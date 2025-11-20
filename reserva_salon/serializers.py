from rest_framework import serializers
from .models import ReservaSalon

class ReservaSalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaSalon
        fields = '__all__'